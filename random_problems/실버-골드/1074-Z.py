import sys
import math
from collections import deque
from itertools import combinations
input = sys.stdin.readline

def Z(N ,r,c):
    global cnt
    if N == 1: #N이 1이면 일단 패스
        if r==0 and c==0:
            cnt += 0
        elif r == 0 and c==1:
            cnt += 1
        elif r == 1 and c==0:
            cnt += 2
        elif r == 1 and c==1:
            cnt += 3
    # 사각형4개로 나눠서 재귀호출
    elif N >= 2:
        half = (2**N) //2
        half_mul = half * half
        if r < half and c < half:
            Z(N-1, r, c)
        elif r < half and c >= half:
            cnt += half_mul * 1
            Z(N-1, r, c-half)
        elif r >= half and c < half:
            cnt += half_mul * 2
            Z(N-1, r-half, c)
        elif r >= half and c >= half:
            cnt += half_mul * 3
            Z(N-1, r-half, c-half)
        

N,r,c = map(int,input().split())
cnt = 0
Z(N,r,c)
print(cnt)
# for row in square:
#     print(*row)
