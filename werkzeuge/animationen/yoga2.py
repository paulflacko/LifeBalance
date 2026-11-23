# Neue Yoga-Haltungen (2026-11): Kobra, Vorbeuge sitzend, Schmetterling, Stuhl, Girlande, Baum, Dreieck
import sys; sys.path.insert(0, '.')
from poses import *
def lp(a, b, t): return (lerp(a[0], b[0], t), lerp(a[1], b[1], t))
def leg(r, n): return r['limbs'][n]
def thigh(r, n, a=0.1, b=0.75, w=26): g = leg(r, n); return (lp(g['root'], g['j1'], a), lp(g['root'], g['j1'], b), w)
def spine(r, a=0.1, b=0.9, w=30): return (lp(r['P'], r['S'], a), lp(r['P'], r['S'], b), w)
def dot(p, w=44): return (p, p, w)
NEWA = {}; NEWV = {}; NEWG = {}

# Kobra: Bauchlage, Kopf rechts, Oberkörper hebt sich auf die Hände
def cobra(up):
    P = (0, -20)
    q = pose(P=P, t=-2 - 30 * up, b=-14 * up, n=-8 - 50 * up, leg1=A(179, 180, 180), leg2=A(178, 180, 180),
             s={'leg1ft': .7, 'leg2ft': .7})
    S = resolve(q)['S']
    q['arm1'] = K(S[0] - 4 + 14 * up, -6, 1); q['arm2'] = K(S[0] - 10 + 14 * up, -6, 1)
    return q
NEWA['yoga-kobra'] = [(cobra(0), 800, 1300), (cobra(1), 1800, 1300)]
NEWG['yoga-kobra'] = lambda r: [spine(r, .0, .5, 32)]

# Vorbeuge sitzend: Beine lang nach rechts, mit langem Rücken nach vorn
def seatfold(f):
    P = (-40, -24)
    q = pose(P=P, t=-90 + 62 * f, b=14 * f, n=-90 + 85 * f, leg1=A(0, 0, -80), leg2=A(-1, 0, -80))
    q['arm1'] = K(30 + 150 * f, -8 - 18 * f, 1); q['arm2'] = K(24 + 150 * f, -8 - 18 * f, 1)
    return q
NEWA['yoga-vorbeuge-sitzend'] = [(seatfold(0), 900, 1400), (seatfold(1), 1800, 1400)]
NEWG['yoga-vorbeuge-sitzend'] = lambda r: [thigh(r, 'leg1', .2, .95, 24), spine(r, .0, .4, 28)]

# Stuhl: aus dem Stand mit Armen hoch in die Hocke, Hüfte nach hinten
def chair(d):
    P = (-10 - 46 * d, -204 + 80 * d)
    q = pose(P=P, t=-90 + 34 * d, n=-90 + 26 * d, leg1=K(4, -10, -1, 0), leg2=K(0, -10, -1, 0),
             arm1=A(-90 + 34 * d - 6, -90 + 34 * d - 8), arm2=A(-90 + 34 * d - 2, -90 + 34 * d - 4))
    return q
NEWA['yoga-stuhl'] = [(chair(0), 700, 1200), (chair(1), 2000, 1200)]
NEWG['yoga-stuhl'] = lambda r: [thigh(r, 'leg1', .05, .9, 28)]

# Girlande (tiefe Hocke), Hände vor der Brust, Ellbogen schieben Knie nach außen
def garland(b):
    P = (-30, -46 - 4 * b)
    q = pose(P=P, t=-80 - 4 * b, n=-86, leg1=K(30, -10, -1, 0), leg2=K(24, -10, -1, 0))
    S = resolve(q)['S']
    q['arm1'] = K(S[0] + 34, S[1] + 40, 1); q['arm2'] = K(S[0] + 30, S[1] + 42, 1)
    return q
NEWA['yoga-girlande'] = [(garland(0), 1200, 1600), (garland(1), 1200, 1600)]
NEWG['yoga-girlande'] = lambda r: [dot(r['P'], 50)]

# Baum (Frontansicht): Fuß an die Innenseite des Standbeins, Arme hoch
def tree(up):
    q = pose(hipoff=12, shoff=26, leg2=A(92, 90, 0), leg1=A(160, 38, 10),
             arm1=A(110 - 220 * up if up else 120, -40 if up else -10), arm2=A(70 + 220 * up if up else 60, 220 if up else 190),
             s={'leg1th': .82, 'leg1sh': .9, 'leg2ft': .5, 'leg1ft': .5})
    if up:
        q['arm1'] = A(-100, -82); q['arm2'] = A(-80, -98)
    else:
        q['arm1'] = A(128, -28); q['arm2'] = A(52, 208)
    return q
NEWA['yoga-baum'] = [(tree(0), 1000, 1300), (tree(1), 2000, 1300)]
NEWV['yoga-baum'] = 'front'
NEWG['yoga-baum'] = lambda r: [thigh(r, 'leg1', .0, .7, 24)]

# Dreieck (Frontansicht): breiter Stand, Oberkörper seitlich über das vordere Bein, Arme eine Linie
def tri(d):
    t = -90 + 70 * d
    q = pose(P=(-6, -176), t=t, n=t, hipoff=14, shoff=26, leg1=K(-120, -10, 1, 180), leg2=K(112, -10, -1, 30),
             arm1=A(t - 90 if d else 180, t - 90 if d else 180), arm2=A(t + 90 if d else 0, t + 90 if d else 0))
    return q
NEWA['yoga-dreieck'] = [(tri(0), 900, 1400), (tri(1), 2000, 1400)]
NEWV['yoga-dreieck'] = 'front'
NEWG['yoga-dreieck'] = lambda r: [thigh(r, 'leg2', .1, .9, 22), spine(r, .3, 1.0, 22)]

# Schmetterling (Frontansicht, sitzend): Fußsohlen zusammen, Knie sinken
def fly(d):
    a = 168 - 14 * d
    q = pose(P=(0, -30), hipoff=14, shoff=26, n=-90, leg1=A(a, 180 - a + 4, 0), leg2=A(180 - a, a - 4, 180),
             s={'leg1th': .85, 'leg2th': .85, 'leg1sh': .62, 'leg2sh': .62, 'leg1ft': .4, 'leg2ft': .4})
    r = resolve(q); f1, f2 = r['limbs']['leg1']['j2'], r['limbs']['leg2']['j2']
    q['arm1'] = K(f1[0] - 4, f1[1] - 8, -1); q['arm2'] = K(f2[0] + 4, f2[1] - 8, 1)
    return q
NEWA['yoga-schmetterling'] = [(fly(0), 900, 1100), (fly(1), 1500, 1100)]
NEWV['yoga-schmetterling'] = 'front'
NEWG['yoga-schmetterling'] = lambda r: [thigh(r, 'leg1', .05, .8, 22), thigh(r, 'leg2', .05, .8, 22)]

if __name__ == '__main__':
    import os; os.makedirs('out3', exist_ok=True)
    for nm in (sys.argv[1:] or NEWA):
        render(NEWA[nm], f'out3/{nm}.gif', view=NEWV.get(nm, 'side'), dur_frame=70, glow=NEWG.get(nm))
