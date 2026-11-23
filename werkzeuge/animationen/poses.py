import sys; sys.path.insert(0,'.')
from fig import *

def A(*a): return {'a': a}
def K(x, y, bend=1, f=0): return {'ik': (x, y), 'bend': bend, 'f': f}
def kneel(P, knee_y=-14, behind=True, f=180, shin=180, nm='leg'):
    dy = -knee_y + P[1]
    dx = math.sqrt(max(0, L['th']**2 - (P[1]-knee_y)**2))
    kx = P[0] - dx if behind else P[0] + dx
    a1 = math.degrees(math.atan2(knee_y - P[1], kx - P[0]))
    return A(a1, shin, f)

ANIM = {}

# ---- Sonnengruß A
stand = pose(arm1=K(26, -268, 1), arm2=K(24, -270, 1))
up = pose(arm1=A(-98, -96), arm2=A(-94, -92), n=-105, b=-8)
fold = pose(P=(-30, -198), t=62, b=26, n=100, arm1=K(34, -2, 1), arm2=K(28, -2, 1), leg1=K(0, -10, -1), leg2=K(0, -10, -1))
half = pose(P=(-28, -198), t=-6, b=0, n=-15, arm1=K(66, -82, -1), arm2=K(60, -82, -1), leg1=K(0, -10, -1), leg2=K(0, -10, -1))
# Plank
plank = pose(P=(-112, -84), t=-21.7, n=-20, arm1=K(4, 0, 1), arm2=K(-2, 0, 1), leg1=K(-292, -12, -1, 25), leg2=K(-292, -12, -1, 25))
chat = pose(P=(-100, -40), t=-4, n=-5, arm1=K(4, -6, 1), arm2=K(-2, -6, 1), leg1=K(-292, -12, -1, 25), leg2=K(-292, -12, -1, 25))
updog = pose(P=(-100, -42), t=-22, b=-32, n=-75, arm1=K(4, -6, 1), arm2=K(-2, -6, 1), leg1=K(-284, -10, -1, 180), leg2=K(-284, -10, -1, 180))
# Hund: Becken aus Dreieck Füße–Hände
def dog(pedal=0):
    Aft, Hd = (-232, -12), (4, -6)
    Pp = pt(Aft, ik(Aft, Hd, 194, 246, -1)[0], 194)
    t = math.degrees(math.atan2(Hd[1]-Pp[1], Hd[0]-Pp[0]))
    l1 = K(-232 + (26 if pedal == 1 else 0), -12 - (26 if pedal == 1 else 0), -1, 0 if pedal != 1 else 40)
    l2 = K(-232 + (26 if pedal == 2 else 0), -12 - (26 if pedal == 2 else 0), -1, 0 if pedal != 2 else 40)
    return pose(P=Pp, t=t, n=t+20, arm1=K(4, -6, 1), arm2=K(-2, -6, 1), leg1=l1, leg2=l2)
ddog = dog()
ANIM['yoga-sonnengruss-a'] = [(stand, 900, 900), (up, 700, 900), (fold, 700, 800), (half, 600, 700), (plank, 600, 600),
    (chat, 400, 600), (updog, 800, 900), (ddog, 1500, 900),
    (pose(**{**half, 'P': (-28, -198)}), 1, 1)]
# zurück: Hund -> Halbe -> Vorbeuge -> Arme hoch -> Stand
ANIM['yoga-sonnengruss-a'] = ANIM['yoga-sonnengruss-a'][:-1] + [(half, 500, 700), (fold, 600, 800), (up, 700, 900)]
ANIM['yoga-herabschauender-hund'] = [(dog(0), 700, 700), (dog(1), 700, 700), (dog(0), 400, 700), (dog(2), 700, 700)]

# ---- Krieger II (Frontansicht)
k2 = pose(P=(10, -132), hipoff=14, shoff=26, leg2=K(150, -10, -1, 0), leg1=K(-140, -10, 1, 180),
          arm1=A(180, 180), arm2=A(0, 0))
rev = pose(P=(10, -132), t=-108, hipoff=14, shoff=26, leg2=K(150, -10, -1, 0), leg1=K(-140, -10, 1, 180),
           arm1=A(108, 98), arm2=A(-112, -118), n=-112)
ANIM['yoga-krieger-2'] = [(k2, 1400, 1100), (rev, 1400, 1100)]

# ---- Tiefer Ausfallschritt
def lunge(Px, Py, t=-92, b=0, arms='knee', n=-92):
    P = (Px, Py)
    arm = {'knee': (K(118, -112, 1), K(114, -114, 1)), 'up': (A(-100, -98), A(-96, -94)), 'hip': (K(Px+10, Py-6, 1), K(Px+6, Py-8, 1))}[arms]
    return pose(P=P, t=t, b=b, n=n, leg1=K(100, -10, -1, 0), leg2=kneel(P), arm1=arm[0], arm2=arm[1])
ANIM['yoga-tiefer-ausfallschritt'] = [(lunge(-2, -100, arms='knee'), 900, 1000), (lunge(16, -86, arms='hip'), 800, 900),
    (lunge(16, -86, t=-95, b=-10, arms='up', n=-105), 1400, 1100)]

# ---- Taube
def pigeon(fold):
    P = (0, -46)
    front = A(math.degrees(math.atan2(32, 92)), 180, 180)
    back = A(math.degrees(math.atan2(32, -92)), 180, 180)
    s = {'leg1sh': 0.55, 'leg1ft': 0.6}
    if not fold:
        return pose(P=P, t=-88, n=-88, leg1=front, leg2=back, s=s, arm1=K(40, -6, 1), arm2=K(34, -6, 1))
    return pose(P=P, t=-14, b=8, n=8, leg1=front, leg2=back, s=s, arm1=K(150, -8, 1), arm2=K(140, -8, 1))
ANIM['yoga-taube'] = [(pigeon(False), 1200, 1300), (pigeon(True), 1800, 1300)]

# ---- Pyramide
def pyr(f):
    P = (-10, -190)
    if not f:
        return pose(P=P, leg1=K(62, -10, -1, 0), leg2=K(-78, -10, 1, -20), arm1=K(-6, -200, 1), arm2=K(-10, -202, 1))
    return pose(P=(-22, -182), t=20, b=40, n=80, leg1=K(62, -10, -1, 0), leg2=K(-78, -10, 1, -20), arm1=K(74, -2, 1), arm2=K(68, -2, 1))
ANIM['yoga-pyramide'] = [(pyr(False), 1000, 1300), (pyr(True), 1800, 1300)]

# ---- Fersensitz / Kindhaltung / Endentspannung
def seiza(breath):
    P = (-22, -48 - breath * 2)
    return pose(P=P, t=-90, b=-breath * 3, n=-90, leg1=kneel(P, behind=False, shin=180), leg2=kneel(P, behind=False, shin=180),
                arm1=K(52, -66, 1), arm2=K(48, -68, 1))
ANIM['yoga-fersensitz'] = [(seiza(0), 900, 1800), (seiza(1), 900, 1800)]
def child(breath):
    P = (-26, -62 - breath * 4)
    return pose(P=P, t=12 - breath*2, b=-breath*2, n=35, leg1=kneel(P, behind=False, shin=180), leg2=kneel(P, behind=False, shin=180),
                arm1=K(212, -8, 1), arm2=K(204, -8, 1))
ANIM['yoga-kindhaltung'] = [(child(0), 900, 1800), (child(1), 900, 1800)]
def sav(breath):
    return pose(P=(0, -24), t=180, b=breath * 3, n=180, face=-1, leg1=A(-1, 0, -75), leg2=A(1, 0, -65), arm1=A(-8, 2), arm2=A(-6, 4))
ANIM['yoga-endentspannung'] = [(sav(0), 1000, 1800), (sav(1), 1000, 1800)]

# ---- Glückliches Baby
def baby(r):
    P = (r * 8, -24)
    k1 = pt(P, -128 + r*3, 98); a1 = pt(k1, -86, 96)
    lg = A(-128 + r*3, -86, 0)
    return pose(P=P, t=180 + r*4, n=180 + r*4, face=-1, leg1=lg, leg2=lg, arm1=K(a1[0], a1[1]-6, 1), arm2=K(a1[0]+4, a1[1]-6, 1))
ANIM['yoga-glueckliches-baby'] = [(baby(-1), 600, 1200), (baby(1), 600, 1200)]

# ---- Katze-Kuh (Vierfüßlerstand)
def quad(t=-10, b=0, n=10, P=(0, -112), arm1=None, arm2=None):
    return pose(P=P, t=t, b=b, n=n, leg1=kneel(P, behind=True, shin=180) if False else A(90, 180, 180), leg2=A(90, 180, 180),
                arm1=arm1 or K(122, -2, 1), arm2=arm2 or K(116, -2, 1))
ANIM['yoga-katze-kuh'] = [(quad(-24, 28, 75), 1000, 1400), (quad(2, -24, -40), 1000, 1400)]
def bws(up):
    n = -40 if up else 30
    q = quad(n=n); r = resolve(q); h = pt(r['head'], n + 180, 2); h = pt(h, n - 90, 26)
    q['arm1'] = K(h[0], h[1], -1 if up else 1); q['arm2'] = K(116, -2, 1)
    return q
ANIM['bws-rotation'] = [(bws(False), 700, 1000), (bws(True), 900, 1000)]

# ---- World's Greatest Stretch
def wgs(stage):
    P = (-8, -84)
    legs = dict(leg1=K(104, -10, -1, 0), leg2=K(-168, -12, -1, 25))
    if stage == 0: return pose(P=P, t=-16, n=-5, arm1=K(132, -6, 1), arm2=K(128, -6, 1), **legs)
    if stage == 1: return pose(P=P, t=-8, b=14, n=20, arm1=A(100, 8), arm2=K(128, -6, 1), **legs)
    return pose(P=P, t=-22, b=-20, n=-75, arm1=A(-92, -90), arm2=K(128, -6, 1), **legs)
ANIM['worlds-greatest-stretch'] = [(wgs(0), 600, 900), (wgs(1), 900, 1000), (wgs(2), 1200, 1000)]
VIEW = {'yoga-krieger-2': 'front'}

PROPS = {}
def topmat(x0, y0, x1, y1):
    def f(pen, r, layer):
        if layer == 'back': pen.rect((x0, y0), (x1, y1), C['mat'])
    return f

# ---- Liegende Drehung (Draufsicht, Kopf links)
def twist(side):
    P = (0, 0)
    if side == 0:
        lg = A(0, 180, 0); s = {'leg1th': 0.45, 'leg2th': 0.45, 'leg1sh': 0.4, 'leg2sh': 0.4, 'leg1ft': .5, 'leg2ft': .5}
        l1 = l2 = lg
    else:
        a = 62 * side
        l1 = A(a, a + 100 * side, a + 100 * side); l2 = A(a - 6 * side, a + 94 * side, a + 94 * side)
        s = {'leg1sh': 0.85, 'leg2sh': 0.85}
    return pose(P=P, t=180, n=180, hipoff=14, shoff=28, leg1=l1, leg2=l2, s=s,
                arm1=A(-90 + 0, -88), arm2=A(90, 88))
ANIM['yoga-liegende-drehung'] = [(twist(0), 500, 1200), (twist(1), 1600, 1200), (twist(0), 500, 1200), (twist(-1), 1600, 1200)]
VIEW['yoga-liegende-drehung'] = 'top'; PROPS['yoga-liegende-drehung'] = topmat(-190, -150, 190, 150)

# ---- Frosch (Draufsicht, Kopf oben)
def frog(back):
    P = (0, 0 + back * 18)
    return pose(P=P, t=-90, n=-90, hipoff=16, shoff=28,
                leg1=A(180 - back * 8, 90, 90), leg2=A(back * 8, 90, 90),
                arm1=A(90, -90), arm2=A(90, -90), s={'arm1ua': .3, 'arm2ua': .3, 'leg1ft': .5, 'leg2ft': .5})
ANIM['yoga-frosch'] = [(frog(0), 1000, 1500), (frog(1), 1400, 1500)]
VIEW['yoga-frosch'] = 'top'; PROPS['yoga-frosch'] = topmat(-170, -230, 170, 160)

# ---- Band Pull-Aparts (Frontansicht)
def band(f, r, layer):
    if layer == 'front':
        a, b = r['limbs']['arm1']['j2'], r['limbs']['arm2']['j2']
        f.line(a, b, 7 * f.k, C['band'])
def pa(open_):
    if not open_:
        return pose(hipoff=12, shoff=26, arm1=A(180, 180), arm2=A(0, 0), leg1=A(95, 92, 180), leg2=A(85, 88, 0),
                    s={'arm1ua': .1, 'arm1fa': .1, 'arm2ua': .1, 'arm2fa': .1, 'leg1ft': .5, 'leg2ft': .5})
    return pose(hipoff=12, shoff=26, arm1=A(180, 180), arm2=A(0, 0), leg1=A(95, 92, 180), leg2=A(85, 88, 0),
                s={'leg1ft': .5, 'leg2ft': .5})
ANIM['band-pull-aparts'] = [(pa(False), 500, 800), (pa(True), 700, 800)]
VIEW['band-pull-aparts'] = 'front'; PROPS['band-pull-aparts'] = band

# ---- Brust-Dehnung am Türrahmen (Seitenansicht, Rahmen hinten)
def frame(pen, r, layer):
    if layer == 'back': pen.rect((-118, -400), (-96, 4), C['wall'])
def chest(lean):
    P = (-10 + lean * 22, -204 + lean * 4)
    return pose(P=P, t=-90 + lean * 10, n=-90 + lean * 10, leg1=K(70, -10, -1, 0) if lean else A(90, 90, 0), leg2=K(-40, -10, 1, 0),
                arm1=K(-96, -300, -1), arm2=A(95, 92))
ANIM['brust-dehnung'] = [(chest(0), 800, 1200), (chest(1), 1600, 1200)]
PROPS['brust-dehnung'] = frame

# ---- Waden-Dehnung an der Wand
def wall(pen, r, layer):
    if layer == 'back': pen.rect((150, -400), (175, 4), C['wall'])
def calf(d):
    P = (0 + d * 14, -196 + d * 4)
    return pose(P=P, t=-72 - 0 * d, n=-75, leg1=K(70, -10, -1, 0), leg2=K(-130, -10, 1, 0),
                arm1=K(150, -270, 1), arm2=K(150, -264, 1))
ANIM['waden-dehnung'] = [(calf(0), 800, 1200), (calf(1), 1600, 1200)]
PROPS['waden-dehnung'] = wall
