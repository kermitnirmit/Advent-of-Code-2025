from copy import deepcopy
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
import utils
import numpy as np
import math


f = [x.strip() for x in open("input.txt").readlines()]
def find_ones_to_remove(b):
    remove_these = []
    for i in range(len(b)):
        for j in range(len(b[i])):
            ns = 0
            if b[i][j] == "@":

                for ni,nj in utils.find_neighbors_2d_8(i, j):
                    if 0 <= ni < len(b) and 0 <= nj< len(b[i]):
                        if b[ni][nj] == "@":
                            ns += 1
                if ns < 4:
                    remove_these.append((i,j))
    return remove_these

def game(board, max_iter=math.inf):
    ans = 0
    iter =0
    while True and iter < max_iter:
        iter += 1
        removals = find_ones_to_remove(board)
        if len(removals) == 0:
            return ans
        ans += len(removals)
        for i, j in removals:
            board[i][j] = "."
    return ans
b = []
for line in f:
    b.append(list(line))
print(game(deepcopy(b), 1))
print(game(deepcopy(b)))

