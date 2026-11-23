import sys; sys.path.insert(0,'.')
from poses import *
for nm in (sys.argv[1:] or ANIM):
    render(ANIM[nm], f'out/{nm}.gif', view=VIEW.get(nm,'side'), props=PROPS.get(nm), dur_frame=80)
