from copy import deepcopy
from collections import defaultdict
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
import utils
import numpy as np
import math


f = [x for x in open("input.txt").readlines()]

problems = defaultdict(list)
for line in f[:-1]:
    nums = utils.ints(line)
    for i, num in enumerate(nums):
        problems[i].append(num)
ans = 0
idx = 0
for op in f[-1].split(" "):
    if not op.strip():
        continue
    op = op.strip()
    if op == "+":
        ans += sum(problems[idx])
    elif op == "*":
        ans += np.prod(problems[idx])
    idx += 1
print(ans)

space_idxs = defaultdict(int)
for line in f:
    for idx, char in enumerate(line):
        if char == " ":
            space_idxs[idx] += 1
split_idxs = []
for idx, count in space_idxs.items():
    if count == len(f):
        split_idxs.append(idx)
split_lines = []
for line in f:
    pieces = []
    prev = 0
    for split_idx in split_idxs:
        pieces.append(line[prev:split_idx])
        prev = split_idx + 1
    pieces.append(line[prev:])
    split_lines.append([p.rstrip('\n') for p in pieces])
problems = defaultdict(list)
for line in split_lines:
    for i, p in enumerate(line):
        problems[i].append(p)
# print(problems)

p2ans = 0
def p2(line):
    nums = []
    max_len = max(len(x) for x in line[:-1])
    for i in range(max_len, -1, -1):
        num = 0
        for elem in line:
            if i < len(elem) and elem[i].isdigit():
                num = num * 10 + int(elem[i])
        if num == 0:
            continue
        nums.append(num)
    if line[-1].strip() == "+":
        return sum(nums)
    elif line[-1].strip() == "*":
        return np.prod(nums)

print(sum(p2(v) for v in problems.values()))
