import sys
import math
from collections import deque
from itertools import combinations
input = sys.stdin.readline

N, M = map(int,input().split())
square = []
for _ in range(N):
    row = list(map(int,input().split()))
    square.append(row)

tetrominoes = [
    # 1. I 모양
    [(0,0),(0,1),(0,2),(0,3)],
    [(0,0),(1,0),(2,0),(3,0)],

    # 2. O 모양
    [(0,0),(0,1),(1,0),(1,1)],

    # 3. L 모양
    [(0,0),(1,0),(2,0),(2,1)],
    [(0,1),(1,1),(2,1),(2,0)],
    [(0,0),(0,1),(1,0),(2,0)],
    [(0,0),(0,1),(1,1),(2,1)],
    [(0,0),(0,1),(0,2),(1,0)],
    [(0,0),(0,1),(0,2),(1,2)],
    [(0,2),(1,0),(1,1),(1,2)],
    [(0,0),(1,0),(1,1),(1,2)],

    # 4. J 모양
    [(0,1),(1,1),(2,1),(2,0)],
    [(0,0),(1,0),(2,0),(2,-1)],
    [(0,0),(0,1),(0,2),(1,2)],
    [(0,0),(0,1),(0,2),(1,0)],

    # 5. S 모양
    [(0,0),(0,1),(1,1),(1,2)],
    [(0,1),(0,2),(1,0),(1,1)],
    [(0,0),(1,0),(1,1),(2,1)],
    [(0,1),(1,0),(1,1),(2,0)],

    # 6. T 모양
    [(0,0),(0,1),(0,2),(1,1)],
    [(0,1),(1,0),(1,1),(2,1)],
    [(0,1),(1,0),(1,1),(1,2)],
    [(0,0),(1,0),(1,1),(2,0)]
]

max_sum = 0

for y in range(N):
    for x in range(M):
        for shape in tetrominoes:
            tmp_sum = 0
            indexerror = False
            for dy,dx in shape:
                ny = y + dy
                nx = x + dx
                if 0<= ny < N and 0<= nx < M:
                    tmp_sum += square[ny][nx]
                else:
                    indexerror = True
                    break
            if indexerror == False:
                max_sum = max(tmp_sum,max_sum)
print(max_sum)
    
            