import sys
from collections import deque
input = sys.stdin.readline

N, K =  map(int,input().split())
Q = deque([i for i in range(1,N+1)])
Josephus = []
while Q:
    for i in range(K-1):
        Q.append(Q.popleft())
    num = Q.popleft()
    Josephus.append(num)



print("<" + ", ".join(map(str, Josephus)) + ">")