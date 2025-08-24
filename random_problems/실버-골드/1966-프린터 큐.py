import sys
from collections import deque
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    N, M = map(int,input().split())
    rank = list(map(int,input().split()))
    Q = deque()
    for i in range(N):
        Q.append([i,rank[i]])
    cnt = 0
    while Q:
        max_rank = 0
        for (idx,rank) in Q:
            max_rank = max(max_rank,rank)

        idx, rank = Q.popleft()
        if rank == max_rank :
            cnt += 1
            if idx == M:
                print(cnt)
                break                
        else:
            Q.append([idx,rank])        

