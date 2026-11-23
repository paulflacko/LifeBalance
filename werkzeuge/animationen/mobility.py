# Zusatz-Animationen für Mobility nach Gefühl: Nacken-Seitneigung und Schulterkreisen (Frontansicht).
import sys; sys.path.insert(0, '.')
from fig import *
def A(*a): return {'a': a}
def front(n=-90, up=1.0, neck=1.0, arms=(95, 92, 85, 88)):
    return pose(hipoff=12, shoff=26, n=n, arm1=A(arms[0], arms[1]), arm2=A(arms[2], arms[3]),
                leg1=A(95, 92, 180), leg2=A(85, 88, 0),
                s={'leg1ft': .5, 'leg2ft': .5, 'up': up, 'neck': neck})
render([(front(), 400, 1100), (front(-118), 1600, 1100), (front(), 400, 1100), (front(-62), 1600, 1100)],
       'out/nacken-seitneigung.gif', view='front', dur_frame=80)
render([(front(), 200, 600), (front(up=1.09, neck=.6), 300, 600), (front(up=1.03, neck=.85, arms=(100, 95, 80, 85)), 200, 600)],
       'out/schulterkreisen.gif', view='front', dur_frame=80)
