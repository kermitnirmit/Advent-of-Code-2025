from copy import deepcopy
from functools import lru_cache
from collections import defaultdict, deque
import sys
from tqdm import trange
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
import utils
import numpy as np
import math


f = [x.strip() for x in open("input.txt").readlines()]

pos = []

for line in f:
    x,y = utils.ints(line)
    pos.append((x,y))

def rect_size(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    width = abs(x2 - x1) + 1
    height = abs(y2 - y1) + 1
    return width * height

def largest_rect(pos):
    largest_rects = []
    for i in range(len(pos)):
        for j in range(i+1, len(pos)):
            x1, y1 = pos[i]
            x2, y2 = pos[j]
            topleft = min(x1,x2), min(y1,y2)
            botright = max(x1,x2), max(y1,y2)
            largest_rects.append((rect_size(pos[i], pos[j]), (topleft, botright)))
    return sorted(largest_rects, reverse=True)

rects_all = largest_rect(pos)
print(rects_all[0][0])

def make_rect(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    top_left = min(x1, x2), min(y1,y2)
    bot_right = max(x1,x2), max(y1,y2)
    return top_left, bot_right


def get_edge_rects(pos):
    ret = []
    p = pos + [pos[0]]
    for l, r in zip(p, p[1:]):
        ret.append(make_rect(l,r))
    return ret


edge_rects = get_edge_rects(pos)

def rect_intersect(r1, r2):
    r1p1, r1p2 = r1
    r2p1, r2p2 = r2
    (x1_min, y1_min), (x1_max, y1_max) = r1p1, r1p2
    (x2_min, y2_min), (x2_max, y2_max) = r2p1, r2p2

    if x1_max <= x2_min or x2_max <= x1_min:
        return False
    if y1_max <= y2_min or y2_max <= y1_min:
        return False
    return True


for (size, r) in rects_all:
    if any(rect_intersect(r, x) for x in edge_rects):
        continue
    else:
        print(size)
        break


