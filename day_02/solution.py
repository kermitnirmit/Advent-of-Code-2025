import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
import utils


f = [x.strip() for x in open("input.txt").readlines()]
pairs = f[0].split(",")
tot1 = 0
tot2 = 0
for pair in pairs:
    s, e = utils.positive_ints(pair)
    for n in range(s, e+1):
        q = str(n)
        if q[:len(q)//2] == q[len(q)//2:]:
            tot1 += n
        l = len(q)
        for k in range(1, l // 2 + 1):
            if l % k == 0:
                section = q[:k]
                if section * (l // k) == q:
                    tot2 += n
                    break
print(tot1)
print(tot2)
