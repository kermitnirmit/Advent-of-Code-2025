import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
import utils
import numpy as np


f = [x.strip() for x in open("input.txt").readlines()]
def largest_subsequence_num(line, k):
    q = [int(x) for x in line]
    drop = len(q) - k
    stack = []
    for num in q:
        while drop > 0 and stack:
            if stack[-1] < num:
                drop -= 1
                stack.pop()
            else:
                break
        stack.append(num)
    return int("".join([str(x) for x in stack[:k]]))
tot1 = 0
tot2 = 0
for line in f:
    tot1 += largest_subsequence_num(line, 2)
    tot2 += largest_subsequence_num(line, 12)
print(tot1)
print(tot2)


