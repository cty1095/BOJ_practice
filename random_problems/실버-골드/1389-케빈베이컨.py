#정점마다 다익스트라돌려서 sum(distance) 비교

import sys
import math
import heapq
from collections import deque
from itertools import combinations
input = sys.stdin.readline

N, M = map(int,input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B =map(int,input().split())
    graph[A].append(B)
    graph[B].append(A)

# for row in graph:
#     print(*row)

def dijkstra(start):
    distance = [float('inf')] * (N+1)
    distance[0] =0
    distance[start] = 0
    heap = []
    heapq.heappush(heap,(0,start))
    while heap:
        now_dist, now_node = heapq.heappop(heap)

        for next_node in graph[now_node]:
            if distance[next_node] > now_dist+1:
                distance[next_node] = now_dist +1
                heapq.heappush(heap,(now_dist+1,next_node))
    
    return sum(distance)


min_kevin = float('inf')
answer = 0
for i in range(1,N+1):
    kevin = dijkstra(i)
    if min_kevin > kevin:
        min_kevin = kevin
        answer = i

print(answer)

