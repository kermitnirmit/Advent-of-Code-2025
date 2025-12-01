import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
import utils


f = [x.strip() for x in open("input.txt").readlines()]
start = 50
c1 = 0
c2 = 0


def move(orig, dir, amt):
    zeros = 0
    sign = 1
    if dir == "L":
        sign = -1
    for _ in range(amt):
        orig += sign
        if orig % 100 == 0:
            zeros += 1
    ended = False
    if orig % 100 == 0:
        ended = True
    return  orig % 100, ended, zeros
for line in f:
    d, amt = line[0], utils.ints(line)[0]
    start, ended, crossed = move(start, d, amt)
    c1 += ended
    c2 += crossed
print(c1)
print(c2)
