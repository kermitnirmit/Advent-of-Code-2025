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


rects = sorted([utils.Rectangle(pos[i], pos[j]) for i in range(len(pos)) for j in range(i+1, len(pos))], key = lambda x : x.area(), reverse=True)
print(rects[0].area())

all_pos = pos + [pos[0]]
edges = [utils.Rectangle(x,y) for x,y in zip(all_pos, all_pos[1:])]

for rect in rects:
    if any(rect.intersect(x) for x in edges):
        continue
    else:
        print(rect.area())
        break
