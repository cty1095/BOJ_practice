import sys
import math
from collections import deque
from itertools import combinations
input = sys.stdin.readline

def bfs(A,B):
    Q = deque()
    Q.append([A,1])
    while Q:
        now, cnt = Q.popleft()
        if now == B:
            return cnt
        if now > B :
            break 
        multiple = now * 2
        str_now=str(now) + "1"
        plus_one = int(str_now)

        if multiple <= B:
            Q.append([multiple,cnt+1])
        if plus_one <= B: 
            Q.append([plus_one,cnt+1])
    return -1

A, B = map(int,input().split())
result = bfs(A,B)
print(result)