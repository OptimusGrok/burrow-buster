# Generates pixel-art Burrow Buster icons (goggled blob in a tunnel).
from PIL import Image, ImageDraw
BLOB=["....RRRRRR....","..RRRRRRRRRR..",".RRRRRRRRRRRR.",".RYYYYRRYYYYR.","RYYWWYYYYWWYYR","RYWWKKYYWWKKYR","RYWWKKYYWWKKYR","RYYWWYYYYWWYYR","RRYYYYRRYYYYRR","RRRRRRRRRRRRRR","RRRRRRRRRRRRRR",".RRRRRRRRRRRR.","..RR..RR..RR..","..RR..RR..RR.."]
C={'R':(232,56,40),'Y':(255,224,64),'W':(255,255,255),'K':(10,10,20)}
def make(size,pad,name,bg_full=True):
    im=Image.new('RGBA',(size,size),(7,7,15,255)); d=ImageDraw.Draw(im)
    # dirt layers
    cols=[(196,120,40),(170,90,30),(140,64,24),(110,44,20)]
    for i,c in enumerate(cols): d.rectangle([0,size*i//4,size,size*(i+1)//4],fill=c+(255,))
    tw=size*0.62; t0=(size-tw)/2
    d.rectangle([t0,t0,t0+tw,t0+tw],fill=(7,7,15,255))
    n=len(BLOB); px=int((size-2*pad)/n); off=(size-px*n)//2
    for y,row in enumerate(BLOB):
        for x,ch in enumerate(row):
            if ch in C: d.rectangle([off+x*px,off+y*px,off+(x+1)*px-1,off+(y+1)*px-1],fill=C[ch]+(255,))
    im.save(name)
import os; o=os.path.dirname(os.path.abspath(__file__))
make(192,40,o+'/icon-192.png'); make(512,106,o+'/icon-512.png')
make(512,150,o+'/icon-maskable-512.png'); make(180,38,o+'/apple-touch-icon.png')
