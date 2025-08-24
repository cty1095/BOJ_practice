import sys
import math
from collections import deque
from itertools import combinations
input = sys.stdin.readline

def two_point(N,M):
    start = 0
    end = 0
    cnt = 0
    while end <= N and start <= end:

        is_M = prefix[end] - prefix[start]
        if is_M == M:
            cnt += 1
            end += 1
        elif is_M > M:
            start += 1
        elif is_M < M:
            end += 1
    return cnt 
        





N, M = map(int,input().split())
list_N = list(map(int,input().split()))
prefix = [0] * (N+1)
for i in range(1,N+1):
    prefix[i] = prefix[i-1] + list_N[i-1]

print(prefix)
cnt = two_point(N,M)
print(cnt)