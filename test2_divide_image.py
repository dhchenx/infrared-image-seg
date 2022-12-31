
# world size [-25 25] [-60 20] [-15 15]
# x-y [-25 25] [-60 20]  (width: 50, height: 80)

from PIL import Image
import os
from itertools import product

def tile(filename, dir_in, dir_out, d):
    name, ext = os.path.splitext(filename)
    img = Image.open(os.path.join(dir_in, filename))
    w, h = img.size

    grid = product(range(0, h - h % d, d), range(0, w - w % d, d))
    for i, j in grid:
        box = (j, i, j + d, i + d)
        out = os.path.join(dir_out, f'{name}_{int(i/d)}_{int(j/d)}{ext}')
        img.crop(box).save(out)

tile("human1.png","data","data/subhuman",150)