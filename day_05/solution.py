from copy import deepcopy
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
import utils
import numpy as np
import math


f = [x.strip() for x in open("input.txt").read().split("\n\n")]
ranges = f[0].split("\n")
others = f[1].split("\n")

r_goods = []
for r in ranges:
    asdf = utils.positive_ints(r)
    r_goods.append([int(x) for x in asdf])

r_goods.sort()
merged = []
for interval in r_goods:
    if not merged or interval[0] > merged[-1][1]:
        merged.append(interval)
    else:
        merged[-1][1] = max(merged[-1][1], interval[1])
r_goods = merged


c = 0
for line in others:
    num = int(line)
    for r in r_goods:
        if r[0] <= num <= r[1]:
            c += 1
print(c)

tot = 0
for lo, hi in r_goods:
    tot += (hi - lo) + 1
print(tot)
