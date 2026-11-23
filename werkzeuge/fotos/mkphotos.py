# Baut aus den free-exercise-db-Fotos (Start/Ende) kleine animierte WebP mit Markierung 1/2.
import sys,json,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from PIL import Image,ImageDraw,ImageFont
from new_ex import NEW,MOB
from map_existing import EXIST
SRC=sys.argv[1]; OUT=sys.argv[2]; os.makedirs(OUT,exist_ok=True)
ids={v[0] if isinstance(v,tuple) else v for v in EXIST.values()}|{r[1] for r in NEW+MOB}
try: F=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',22)
except: F=ImageFont.load_default()
def mark(im,n):
    d=ImageDraw.Draw(im); x,y,r=12,12,17
    d.ellipse([x,y,x+2*r,y+2*r],fill=(255,255,255),outline=(30,30,30),width=2)
    d.text((x+r,y+r),str(n),fill=(30,30,30),font=F,anchor='mm'); return im
tot=0
for i in sorted(ids):
    fr=[]
    for n in (0,1):
        a=Image.open(f'{SRC}/{i}/{n}.jpg').convert('RGB').resize((480,320),Image.LANCZOS)
        fr.append(mark(a,n+1))
    p=f'{OUT}/{i.lower()}.webp'
    fr[0].save(p,save_all=True,append_images=fr[1:],duration=[1400,1400],loop=0,quality=62,method=6)
    tot+=os.path.getsize(p)
print(len(ids),tot//1024,'KB')
