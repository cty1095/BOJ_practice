import sys
import math
import heapq
from collections import deque
from itertools import combinations
input = sys.stdin.readline

N = int(input())
top_height = list(map(int,input().split()))
stack= []
received = [0] * (N)

for i in range(N-1,-1,-1):  # 왼 <- 오 순
    while stack and top_height[stack[-1]] < top_height[i]:
        idx = stack.pop()
        received[idx] = i+1

    if len(stack) == 0 or top_height[stack[-1]] >= top_height[i]:
        stack.append(i)
print(*received)
