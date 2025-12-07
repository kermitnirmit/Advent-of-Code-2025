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


def search(splitters, start):
    seen = set()
    def dfs(curr):
        if curr in seen or curr[0] >= len(f):
            return 0
        seen.add(curr)
        if curr in splitters:
            next_left = (curr[0], curr[1]-1)
            next_right = (curr[0], curr[1] + 1)
            return 1 + dfs(next_left) + dfs(next_right)
        else:
            next_down = (curr[0] + 1, curr[1])
            return dfs(next_down)
    return dfs(start)

def search2(splitters, start):
    @lru_cache(maxsize = None)
    def dfs(curr):
        if curr[0] >= len(f):
            return 0
        if curr in splitters:
            next_left = (curr[0], curr[1]-1)
            next_right = (curr[0], curr[1] + 1)
            return 1 + dfs(next_left) + dfs(next_right)
        else:
            next_down = (curr[0] + 1, curr[1])
            return dfs(next_down)
    return dfs(start) + 1
         




splits = set()
start = None
for i, line in enumerate(f):
    for j, c in enumerate(line):
        if c == "^":
            splits.add((i,j))
        if c == "S":
            start = (i,j)
print(search(splits, start))
print(search2(splits, start))

# 1741 is too high