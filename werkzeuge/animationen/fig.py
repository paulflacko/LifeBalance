# Eigene Yoga-/Mobility-Animationen: Figur mit Vorwärtskinematik + 2-Gelenk-IK, gerendert mit PIL als GIF.
import math, copy
from PIL import Image, ImageDraw, ImageFilter

SS = 3                      # Supersampling
W, H = 600, 400
FLOOR = 380                 # Boden-y im Bild (Seitenansicht)
ZOOM = 1.6                  # größte Vergrößerung: Figur füllt das Bild, besser erkennbar

L = dict(lo=58, up=62, neck=16, head=23, ua=66, fa=62, th=98, sh=96, ft=30, ank=10)
WID = dict(torso=52, ua=20, fa=17, th=36, sh=25, ft=15, neck=16)

C = dict(line=(40, 40, 46), skin=(242, 198, 164), shirt=(222, 226, 234), shorts=(58, 111, 214),
         shoe=(232, 232, 236), hair=(44, 36, 34), mat=(196, 182, 232), band=(240, 140, 50),
         wall=(214, 216, 222), floor=(200, 200, 206))

def dark(c, k=0.82): return tuple(int(v * k) for v in c)
def d2r(a): return math.radians(a)
def pt(o, a, l): return (o[0] + l * math.cos(d2r(a)), o[1] + l * math.sin(d2r(a)))
def lerp(a, b, t): return a + (b - a) * t
def alerp(a, b, t):
    d = (b - a + 180) % 360 - 180
    return a + d * t

def ik(root, target, l1, l2, bend):
    dx, dy = target[0] - root[0], target[1] - root[1]
    d = max(1e-3, min(math.hypot(dx, dy), l1 + l2 - 0.01))
    base = math.degrees(math.atan2(dy, dx))
    c = (l1 * l1 + d * d - l2 * l2) / (2 * l1 * d)
    a = math.degrees(math.acos(max(-1, min(1, c))))
    up = base + bend * a
    e = pt(root, up, l1)
    lo = math.degrees(math.atan2(target[1] - e[1], target[0] - e[0]))
    return up, lo

# Pose: P (Becken, Welt: Boden y=0, oben negativ), t Rumpf, b Rumpfbeugung (oberer Teil relativ),
# n Kopf/Hals, Gliedmaßen leg1/leg2/arm1/arm2 (1 = nah, 2 = fern) als
# {'a':(oben,unten[,fuß])} oder {'ik':(x,y),'bend':±1,'f':fußwinkel}; s = Verkürzungen je Segment.
BASE = dict(P=(0, -204), t=-90, b=0, n=-90,
            leg1={'a': (90, 90, 0)}, leg2={'a': (90, 90, 0)},
            arm1={'a': (95, 92)}, arm2={'a': (86, 88)}, s={}, face=1)

def pose(**kw):
    p = copy.deepcopy(BASE)
    for k, v in kw.items(): p[k] = v
    return p

def resolve(p):
    s = p.get('s', {})
    sc = lambda k: s.get(k, 1.0)
    P = p['P']
    mid = pt(P, p['t'], L['lo'] * sc('lo'))
    S = pt(mid, p['t'] + p['b'], L['up'] * sc('up'))
    hip = {1: P, 2: P}
    sh = {1: S, 2: S}
    if 'hipoff' in p:  # Front-/Draufsicht: Hüfte und Schultern auseinander
        ho, so = p['hipoff'], p['shoff']
        perp = p['t'] + 90
        hip = {1: pt(P, perp, -ho), 2: pt(P, perp, ho)}
        sh = {1: pt(S, perp, -so), 2: pt(S, perp, so)}
    out = dict(P=P, mid=mid, S=S, head=pt(S, p['n'], (L['neck'] + L['head'] * 0.75) * sc('neck')),
               n=p['n'], face=p.get('face', 1), limbs={})
    for nm, root, (k1, k2) in (('leg1', hip[1], ('th', 'sh')), ('leg2', hip[2], ('th', 'sh')),
                               ('arm1', sh[1], ('ua', 'fa')), ('arm2', sh[2], ('ua', 'fa'))):
        spec = p[nm]
        l1, l2 = L[k1] * sc(nm + k1), L[k2] * sc(nm + k2)
        if 'ik' in spec:
            a1, a2 = ik(root, spec['ik'], l1, l2, spec.get('bend', 1))
            f = spec.get('f', 0)
        else:
            a1, a2 = spec['a'][0], spec['a'][1]
            f = spec['a'][2] if len(spec['a']) > 2 else spec.get('f', 0)
        j1 = pt(root, a1, l1); j2 = pt(j1, a2, l2)
        out['limbs'][nm] = dict(root=root, j1=j1, j2=j2, a1=a1, a2=a2, f=f, fs=sc(nm + 'ft'))
    return out

def interp(p, q, t):
    r = copy.deepcopy(p)
    r['P'] = (lerp(p['P'][0], q['P'][0], t), lerp(p['P'][1], q['P'][1], t))
    for k in ('t', 'b', 'n'): r[k] = alerp(p[k], q[k], t)
    for k in ('hipoff', 'shoff'):
        if k in p: r[k] = lerp(p[k], q.get(k, p[k]), t)
    keys = set(p.get('s', {})) | set(q.get('s', {}))
    r['s'] = {k: lerp(p.get('s', {}).get(k, 1), q.get('s', {}).get(k, 1), t) for k in keys}
    rp, rq = resolve(p), resolve(q)
    for nm in ('leg1', 'leg2', 'arm1', 'arm2'):
        a, b = p[nm], q[nm]
        if 'ik' in a and 'ik' in b and a.get('bend', 1) == b.get('bend', 1):
            r[nm] = {'ik': (lerp(a['ik'][0], b['ik'][0], t), lerp(a['ik'][1], b['ik'][1], t)),
                     'bend': a.get('bend', 1), 'f': alerp(a.get('f', 0), b.get('f', 0), t)}
        else:
            la, lb = rp['limbs'][nm], rq['limbs'][nm]
            r[nm] = {'a': (alerp(la['a1'], lb['a1'], t), alerp(la['a2'], lb['a2'], t), alerp(la['f'], lb['f'], t))}
    return r

def ease(t): return 0.5 - 0.5 * math.cos(math.pi * t)

# ---------------------------------------------------------------- Zeichnen
class Pen:
    def __init__(self, ox, oy, scale):
        self.im = Image.new('RGB', (W * SS, H * SS), (255, 255, 255))
        self.d = ImageDraw.Draw(self.im)
        self.ox, self.oy, self.k = ox, oy, scale
    def X(self, p): return ((self.ox + p[0] * self.k) * SS, (self.oy + p[1] * self.k) * SS)
    def cap(self, a, b, w, fill, outline=True):
        w = w * self.k * SS
        A, B = self.X(a), self.X(b)
        for col, ww in ((C['line'], w + 5 * SS), (fill, w)) if outline else ((fill, w),):
            self.d.line([A, B], fill=col, width=int(ww))
            r = ww / 2
            for q in (A, B): self.d.ellipse([q[0] - r, q[1] - r, q[0] + r, q[1] + r], fill=col)
    def caps(self, segs):  # zusammenhängende Gliedmaße: erst alle Konturen, dann Füllungen
        for a, b, w, f in segs: self.cap_one(a, b, w, C['line'], 5)
        for a, b, w, f in segs: self.cap_one(a, b, w, f, 0)
    def cap_one(self, a, b, w, col, extra):
        ww = w * self.k * SS + extra * SS
        A, B = self.X(a), self.X(b)
        self.d.line([A, B], fill=col, width=int(ww))
        r = ww / 2
        for q in (A, B): self.d.ellipse([q[0] - r, q[1] - r, q[0] + r, q[1] + r], fill=col)
    def circle(self, c, r, fill, outline=True):
        X = self.X(c); r = r * self.k * SS
        if outline: self.d.ellipse([X[0] - r - 2.5 * SS, X[1] - r - 2.5 * SS, X[0] + r + 2.5 * SS, X[1] + r + 2.5 * SS], fill=C['line'])
        self.d.ellipse([X[0] - r, X[1] - r, X[0] + r, X[1] + r], fill=fill)
    def rect(self, a, b, fill):
        A, B = self.X(a), self.X(b)
        self.d.rounded_rectangle([min(A[0], B[0]), min(A[1], B[1]), max(A[0], B[0]), max(A[1], B[1])], radius=3 * SS, fill=fill)
    def line(self, a, b, w, col):
        self.d.line([self.X(a), self.X(b)], fill=col, width=int(w * SS))
    def out(self): return self.im.resize((W, H), Image.LANCZOS)

def draw_leg(pen, lg, far, view):
    k = 0.84 if far else 1
    skin, shorts, shoe = dark(C['skin'], k), dark(C['shorts'], k), dark(C['shoe'], k)
    hipj, knee, ank = lg['root'], lg['j1'], lg['j2']
    shorts_end = pt(hipj, lg['a1'], L['th'] * 0.36 * (math.dist(hipj, knee) / L['th']))
    fl = L['ft'] * lg['fs']
    heel, toe = pt(ank, lg['f'] + 180, 7 * lg['fs']), pt(ank, lg['f'], fl)
    pen.caps([(hipj, knee, WID['th'] * 0.9, skin), (knee, ank, WID['sh'], skin), (heel, toe, WID['ft'], shoe)])
    pen.cap(hipj, shorts_end, WID['th'] + 3, shorts)

def draw_arm(pen, lg, far):
    k = 0.84 if far else 1
    skin = dark(C['skin'], k)
    pen.caps([(lg['root'], lg['j1'], WID['ua'], skin), (lg['j1'], lg['j2'], WID['fa'], skin)])
    pen.circle(pt(lg['j1'], lg['a2'], L['fa'] * 0.02), 0, skin, outline=False)

def draw_head(pen, r, view):
    hc, n = r['head'], r['n']
    R = L['head']
    if view == 'top':
        pen.circle(hc, R, C['hair']); return
    pen.circle(hc, R, C['hair'])
    if view == 'front':
        sk = pt(hc, n + 180, 5)
        pen.circle(sk, R - 5, C['skin'], outline=False)
        for s in (-1, 1):
            e = pt(pt(hc, n + 90, 8 * s), n + 180, 2)
            pen.circle(e, 2.2, C['line'], outline=False)
        return
    fd = n + 90 * r['face']
    pen.circle(pt(pt(hc, fd, 5), n + 180, 4), R - 4, C['skin'], outline=False)
    pen.circle(pt(pt(hc, fd, R - 1), n + 180, 2), 4.5, C['skin'], outline=False)  # Nase
    pen.circle(pt(pt(hc, fd, R * 0.55), n, 3), 2.3, C['line'], outline=False)    # Auge
    pen.circle(pt(pt(hc, fd, -R * 0.15), n + 180, 2), 5, dark(C['skin'], .9), outline=False)  # Ohr

def draw_body(pen, r, view='side'):
    lm = r['limbs']
    far = view == 'side'
    draw_arm(pen, lm['arm2'], far)
    draw_leg(pen, lm['leg2'], far, view)
    # Rumpf
    P, mid, S = r['P'], r['mid'], r['S']
    pen.cap(S, pt(S, r['n'], L['neck']), WID['neck'], C['skin'])
    tw = WID['torso'] + (14 if view in ('front', 'top') else 0)
    pen.caps([(P, mid, tw, C['shirt']), (mid, S, tw + 3, C['shirt'])])
    pen.cap(P, pt(P, math.degrees(math.atan2(mid[1] - P[1], mid[0] - P[0])), L['lo'] * 0.35), tw + 3, C['shorts'])
    draw_leg(pen, lm['leg1'], False, view)
    if view in ('front', 'top'):  # Shorts über beide Oberschenkelansätze
        for nm in ('leg1', 'leg2'):
            lg = lm[nm]
            pen.cap(lg['root'], pt(lg['root'], lg['a1'], 30), WID['th'] + 4, C['shorts'])
        pen.cap(lm['leg1']['root'], lm['leg2']['root'], tw - 6, C['shorts'], outline=False)
    draw_head(pen, r, view)
    draw_arm(pen, lm['arm1'], False)

def bbox(res):
    xs, ys = [], []
    for r in res:
        pts = [r['P'], r['mid'], r['S'], r['head']]
        for lg in r['limbs'].values(): pts += [lg['root'], lg['j1'], lg['j2'], pt(lg['j2'], lg['f'], L['ft'])]
        xs += [p[0] for p in pts]; ys += [p[1] for p in pts]
    return min(xs) - 30, min(ys) - 30, max(xs) + 30, max(ys) + 14

GLOW = (255, 84, 54)
def glow_layer(im, pen, segs, strength):
    # Weich leuchtender Zielbereich (wo es dehnen bzw. arbeiten soll), pulsiert über die Animation
    m = Image.new('L', im.size, 0); d = ImageDraw.Draw(m)
    for a, b, w in segs:
        A, B = pen.X(a), pen.X(b); ww = w * pen.k * SS
        d.line([A, B], fill=255, width=int(ww)); r = ww / 2
        for q in (A, B): d.ellipse([q[0] - r, q[1] - r, q[0] + r, q[1] + r], fill=255)
    m = m.filter(ImageFilter.GaussianBlur(5 * SS)).point(lambda v: int(v * strength))
    im.paste(Image.new('RGB', im.size, GLOW), (0, 0), m)

def render(keys, path, view='side', props=None, dur_frame=70, scale=None, floor=True, mat=True, glow=None):
    """keys: Liste aus (pose, halten_ms, übergang_ms). Letzte Pose geht zurück zur ersten."""
    frames = []   # (pose, dauer)
    n = len(keys)
    for i, (p, hold, tr) in enumerate(keys):
        frames.append((p, hold))
        q = keys[(i + 1) % n][0]
        steps = max(1, round(tr / dur_frame))
        for s in range(1, steps):
            frames.append((interp(p, q, ease(s / steps)), dur_frame))
    res = [resolve(f[0]) for f in frames]
    x0, y0, x1, y1 = bbox(res)
    if view == 'side' and floor: y1 = 4
    k = scale or min(ZOOM, (W - 36) / (x1 - x0), (H - 24) / (y1 - y0))
    ox = W / 2 - (x0 + x1) / 2 * k
    oy = (FLOOR - 0 * k) if (view == 'side' and floor) else H / 2 - (y0 + y1) / 2 * k
    imgs = []; total = sum(d for _, d in frames); acc = 0
    for (p, d), r in zip(frames, res):
        ph = acc / total; acc += d
        pen = Pen(ox, oy, k)
        if view == 'side' and floor:
            pen.line(((0 - ox) / k, 4), ((W - ox) / k, 4), 3, C['floor'])
            if mat: pen.rect((x0 + 10, -1), (x1 - 10, 5), C['mat'])
        if props: props(pen, r, 'back')
        draw_body(pen, r, view)
        if props: props(pen, r, 'front')
        if glow: glow_layer(pen.im, pen, glow(r), 0.6 + 0.3 * (0.5 - 0.5 * math.cos(2 * math.pi * 2 * ph)))
        imgs.append((pen.out(), d))
    # Palette aus mehreren Bildern, damit das Leuchten in allen Stärken sauber bleibt
    sheet = Image.new('RGB', (W, H * min(4, len(imgs))))
    for j in range(min(4, len(imgs))): sheet.paste(imgs[j * len(imgs) // min(4, len(imgs))][0], (0, H * j))
    pl = sheet.quantize(colors=63 if glow else 39, method=Image.MEDIANCUT).getpalette()[:(63 if glow else 39) * 3] + [255, 255, 255]
    for j in range(0, len(pl), 3):  # fast-weiß ist weiß (Pillow sucht Paletten nur näherungsweise)
        if min(pl[j:j + 3]) >= 246: pl[j:j + 3] = [255, 255, 255]
    ref = Image.new('P', (1, 1)); ref.putpalette(pl + [255, 255, 255] * (256 - len(pl) // 3))
    pal = [im.quantize(palette=ref, dither=Image.Dither.NONE) for im, _ in imgs]
    pal[0].save(path, save_all=True, append_images=pal[1:], duration=[d for _, d in imgs], loop=0, optimize=True, disposal=1)
    return imgs

def still(p, path, view='side', **kw):
    imgs = render([(p, 1000, 0)], path.replace('.png', '.gif'), view, **kw)
    imgs[0][0].save(path)
