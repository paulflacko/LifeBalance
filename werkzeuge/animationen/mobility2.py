# Mobility-Animationen mit leuchtendem Zielbereich (zeigt, wo es dehnen bzw. arbeiten soll) + neue eigene Animationen
import sys; sys.path.insert(0, '.')
from poses import *
from mobility import front as nfront
def lp(a, b, t): return (lerp(a[0], b[0], t), lerp(a[1], b[1], t))
def leg(r, n): return r['limbs'][n]
def thigh(r, n, a=0.1, b=0.75, w=26): g = leg(r, n); return (lp(g['root'], g['j1'], a), lp(g['root'], g['j1'], b), w)
def shin(r, n, w=22): g = leg(r, n); return (lp(g['j1'], g['j2'], .15), lp(g['j1'], g['j2'], .8), w)
def spine(r, a=0.1, b=0.9, w=30): return (lp(r['P'], r['S'], a), lp(r['P'], r['S'], b), w)
def dot(p, w=44): return (p, p, w)

G = {
 'yoga-katze-kuh': lambda r: [spine(r)],
 'bws-rotation': lambda r: [spine(r, .45, 1.0, 34)],
 'worlds-greatest-stretch': lambda r: [thigh(r, 'leg2', .05, .6), spine(r, .5, 1.0, 26)],
 'yoga-tiefer-ausfallschritt': lambda r: [thigh(r, 'leg2', .0, .6, 30)],
 'yoga-taube': lambda r: [dot(lp(r['P'], leg(r, 'leg1')['j1'], .18), 50)],
 'yoga-pyramide': lambda r: [thigh(r, 'leg1', .15, .9, 24)],
 'yoga-herabschauender-hund': lambda r: [thigh(r, 'leg1', .2, .9, 22), shin(r, 'leg1', 18)],
 'yoga-kindhaltung': lambda r: [spine(r, .0, .55, 34)],
 'yoga-frosch': lambda r: [thigh(r, 'leg1', .05, .8, 22), thigh(r, 'leg2', .05, .8, 22)],
 'yoga-liegende-drehung': lambda r: [spine(r, .0, .5, 34)],
 'yoga-glueckliches-baby': lambda r: [dot(r['P'], 56)],
 'yoga-krieger-2': lambda r: [thigh(r, 'leg1', .0, .55, 24), thigh(r, 'leg2', .0, .55, 24)],
 'brust-dehnung': lambda r: [dot(lp(r['S'], r['mid'], .3), 46), (leg(r, 'arm1')['root'], lp(leg(r, 'arm1')['root'], leg(r, 'arm1')['j1'], .5), 18)],
 'waden-dehnung': lambda r: [shin(r, 'leg2', 22)],
 'band-pull-aparts': lambda r: [dot(leg(r, 'arm1')['root'], 30), dot(leg(r, 'arm2')['root'], 30)],
 'yoga-fersensitz': None, 'yoga-endentspannung': None, 'yoga-sonnengruss-a': None,
}
for nm, g in G.items():
    render(ANIM[nm], f'out2/{nm}.gif', view=VIEW.get(nm, 'side'), props=PROPS.get(nm), dur_frame=70, glow=g)

# Nacken und Schultern (Frontansicht)
def neckg(r):
    side = 1 if r['head'][0] < r['S'][0] else -1   # Kopf nach links geneigt -> rechte Halsseite dehnt
    sh = pt(r['S'], 0, 24 * side)
    return [(sh, lp(sh, r['head'], .7), 22)]
render([(nfront(), 400, 1100), (nfront(-118), 1600, 1100), (nfront(), 400, 1100), (nfront(-62), 1600, 1100)],
       'out2/nacken-seitneigung.gif', view='front', dur_frame=70, glow=neckg)
render([(nfront(), 200, 600), (nfront(up=1.09, neck=.6), 300, 600), (nfront(up=1.03, neck=.85, arms=(100, 95, 80, 85)), 200, 600)],
       'out2/schulterkreisen.gif', view='front', dur_frame=70,
       glow=lambda r: [dot(leg(r, 'arm1')['root'], 30), dot(leg(r, 'arm2')['root'], 30)])

# NEU: Hüftbeuger-Dehnung kniend (Becken nach vorn schieben, Po fest)
hf0 = lunge(-6, -104, arms='hip'); hf1 = lunge(18, -90, t=-86, arms='hip', n=-88)
render([(hf0, 700, 1100), (hf1, 1800, 1100)], 'out2/hueftbeuger-dehnung.gif', dur_frame=70,
       glow=lambda r: [thigh(r, 'leg2', .0, .55, 30)])

# NEU: Hüftbrücke (Rückenlage, Kopf links, Füße rechts aufgestellt)
def bridge(up):
    P = (0, -26 - up * 84)
    t = 180 - up * 24
    q = pose(P=P, t=t, n=t, face=-1, leg1=K(104, -10, -1, 0), leg2=K(100, -10, -1, 0))
    S = resolve(q)['S']; q['arm1'] = K(S[0] + 124, -9, -1); q['arm2'] = K(S[0] + 122, -9, -1)
    return q
render([(bridge(0), 600, 1000), (bridge(1), 1300, 1000)], 'out2/hueftbruecke.gif', dur_frame=70,
       glow=lambda r: [dot(r['P'], 52)])

# NEU: Bird Dog (Vierfüßler, Gegenarm und -bein strecken)
def bd(ext):
    q = quad(t=-6 + 0 * ext, n=0)
    if ext:
        q['arm1'] = A(-6, -4); q['leg2'] = A(184, 182, 120)
    return q
render([(bd(0), 500, 900), (bd(1), 1500, 900)], 'out2/bird-dog.gif', dur_frame=70,
       glow=lambda r: [spine(r, .0, .45, 30), dot(r['P'], 36)])
