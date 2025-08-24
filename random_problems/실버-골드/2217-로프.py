import sys
import math
from collections import deque
input = sys.stdin.readline


N = int(input())


ropes = []

for _ in range(N):
    rope = int(input())
    ropes.append(rope)

ropes.sort()
max_weight = 0
for i in range(N):
    weight = ropes[i] * (N-i)
    max_weight = max(max_weight,weight)

print(max_weight)