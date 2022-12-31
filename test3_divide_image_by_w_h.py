
# world size [-25 25] [-60 20] [-15 15]
# x-y [-25 25] [-60 20]  (width: 50, height: 80)

from PIL import Image
import os
from itertools import product

def tile(filename, dir_in, dir_out, num_w,num_h):
    name, ext = os.path.splitext(filename)
    img = Image.open(os.path.join(dir_in, filename))
    w, h = img.size
    d_w=int(w/num_w)
    d_h=int(h/num_h)

    grid = product(range(0, h - h % d_h, d_h), range(0, w - w % d_w, d_w))
    for i, j in grid:
        box = (j, i, j + d_h, i + d_w)
        out = os.path.join(dir_out, f'{name}_{int(i/d_h)}_{int(j/d_w)}{ext}')
        img.crop(box).save(out)

tile("human1.png","data","data/subhuman2",4,4)