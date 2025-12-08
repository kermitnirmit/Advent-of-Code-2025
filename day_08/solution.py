from copy import deepcopy
from functools import lru_cache
from collections import defaultdict, deque
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
import utils
import numpy as np
import math


f = [x.strip() for x in open("input.txt").readlines()]

pos = []

for line in f:
    x,y,z = utils.ints(line)
    pos.append((x,y,z))

pairwise_dists = {}
for i in range(len(pos)):
    for j in range(i + 1, len(pos)):
        pos1 = pos[i]
        pos2 = pos[j]
        dist = utils.euclidean_distance(pos1, pos2)
        pairwise_dists[(i, j)] = dist
import heapq

heap = []
for (i, j), dist in pairwise_dists.items():
    heapq.heappush(heap, (dist, i, j))
uf = utils.UnionFind(len(pos))
for q in range(len(heap)):
    dist, i, j = heapq.heappop(heap)
    uf.merge(i,j)
    if max(uf.sizes) == len(f):
        x, _, _ = utils.ints(f[i])
        x2, _, _ = utils.ints(f[j])
        print(x * x2)
        break
    if q == 999:
        print(np.prod(sorted(uf.sizes, reverse=True)[:3]))
