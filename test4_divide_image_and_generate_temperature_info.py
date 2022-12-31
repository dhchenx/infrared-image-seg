
# world size [-25 25] [-60 20] [-15 15]
# x-y [-25 25] [-60 20]  (width: 50, height: 80) d=5, (50, 16)

from PIL import Image
import os
from itertools import product
import random
import numpy
from quickcsv import *

list_model=[]

def tile(filename, dir_in, dir_out, num_w,size):
    name, ext = os.path.splitext(filename)
    img = Image.open(os.path.join(dir_in, filename))
    w, h = img.size

    d=int(w/num_w)
    size=50/num_w

    grid = product(range(0, h - h % d, d), range(0, w - w % d, d))
    for i, j in grid:
        box = (j, i, j + d, i + d)
        a = int(i/d)
        b = int(j/d)
        out = os.path.join(dir_out, f'{name}_{a}_{b}{ext}')
        img.crop(box).save(out)
        color = get_point_color(out)
        x_min=-25+a*size
        x_max=-25+(a+1)*size
        y_min=20-b*size
        y_max=20-(b+1)*size
        model={
            "x_min": x_min,
            "x_max":x_max,
            "y_min": y_max,
            "y_max":y_min,
            "r":color[0],
            "g":color[1],
            "b":color[2]
        }
        list_model.append(model)
    write_csv("infrared-data-detail.csv",list_model)

def get_point_color(path):
    img = Image.open(path)
    w, h = img.size
    w1=random.randint(0, w-1)
    h1=random.randint(0,h-1)
    pixel_values=list(img.getdata())
    pixel_values = numpy.array(pixel_values).reshape((w, h, 3))
    rgba=pixel_values[w1][h1]
    # print("color1:", rgba)
    return rgba

tile("human1.png","data","data/subhuman3",50,1)