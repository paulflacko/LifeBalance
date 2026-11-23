# Animationen für den Einstieg: Aufwärmsätze (Kreuzheben mit wachsender Last) und Unterarmstütz.
import sys; sys.path.insert(0, '.')
from fig import *
from PIL import ImageFont

def K(x, y, bend=1, f=0): return {'ik': (x, y), 'bend': bend, 'f': f}
def A(*a): return {'a': a}

# ---- Aufwärmsätze: Kreuzheben von Schienbeinhöhe, Scheiben wachsen in 3 Stufen
BAR_X = 22
def lift(top, r):
    by = -max(48, r) if not top else -150      # Stangenhöhe (Mitte)
    if top:
        return pose(P=(-8, -204), t=-90, n=-88, leg1=K(0, -10, -1), leg2=K(0, -10, -1),
                    arm1=K(BAR_X - 14, by, 1), arm2=K(BAR_X - 18, by, 1))
    return pose(P=(-62, -128), t=-28, b=-4, n=-30, leg1=K(4, -10, -1), leg2=K(4, -10, -1),
                arm1=K(BAR_X, by, 1), arm2=K(BAR_X - 4, by, 1))

def plates(r):
    def draw(pen, res, layer):
        if layer != 'front': return
        h = res['limbs']['arm1']['j2']
        c = (h[0], h[1])
        if r:
            pen.circle(c, r, (52, 58, 70))
            pen.circle(c, r * 0.72, (70, 78, 92), outline=False)
        pen.circle(c, 7, (170, 172, 180))
    return draw

FONT = None
for f in ('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', '/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf'):
    try: FONT = ImageFont.truetype(f, 30); FONT2 = ImageFont.truetype(f.replace('-Bold', ''), 20); break
    except Exception: pass

def label(im, big, small):
    d = ImageDraw.Draw(im)
    d.text((24, 18), big, fill=(40, 40, 46), font=FONT)
    d.text((24, 56), small, fill=(110, 110, 120), font=FONT2)
    return im

stages = [(0, '8 Wdh.', 'leere Stange'), (30, '5 Wdh.', 'ca. 50 % vom Arbeitsgewicht'), (46, '3 Wdh.', 'ca. 75 % vom Arbeitsgewicht')]
frames = []
for r, big, small in stages:
    keys = [(lift(False, r), 350, 700), (lift(True, r), 350, 700)]
    imgs = render(keys, '/tmp/_st.gif', props=plates(r), dur_frame=80, scale=0.78)
    reps = 2
    for _ in range(reps):
        frames += [(label(im.copy(), big, small), d) for im, d in imgs]
    frames[-1] = (frames[-1][0], 900)

def save(frames, path):
    pl = frames[-1][0].quantize(colors=47, method=Image.MEDIANCUT).getpalette()[:141] + [255, 255, 255]
    for j in range(0, len(pl), 3):
        if min(pl[j:j + 3]) >= 246: pl[j:j + 3] = [255, 255, 255]
    ref = Image.new('P', (1, 1)); ref.putpalette(pl + [255, 255, 255] * (256 - 48))
    pal = [im.quantize(palette=ref, dither=Image.Dither.NONE) for im, _ in frames]
    pal[0].save(path, save_all=True, append_images=pal[1:], duration=[d for _, d in frames], loop=0, optimize=True, disposal=1)

save(frames, 'out/aufwaermsaetze.gif')

# ---- Unterarmstütz: gerade Linie, ruhiges Atmen
def fplank(br):
    ank = (-305, -10); S = (0, -76)
    ang = math.degrees(math.atan2(S[1] - ank[1], S[0] - ank[0]))
    P = pt(ank, ang, 194)
    P = (P[0], P[1] - br)
    t = math.degrees(math.atan2(S[1] - P[1], S[0] - P[0]))
    return pose(P=P, t=t, n=t + 8, leg1=K(*ank, -1, 25), leg2=K(ank[0] + 4, ank[1], -1, 25),
                arm1=A(90, 0), arm2=A(92, 2))
render([(fplank(0), 600, 1500), (fplank(3), 600, 1500)], 'out/unterarmstuetz.gif', dur_frame=100)
