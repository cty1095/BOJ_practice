#프림 알고리즘 사용

import sys
import math
import heapq
from collections import deque
from itertools import combinations
input = sys.stdin.readline

V, E = map(int,input().split())

graph = [[] for _ in range(V+1)]

for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def prime():
    start = 1 #임의로 1에서 시작
    visited = [False] * (V+1)
    heap = []
    weight = 0
    heapq.heappush(heap,(0,start))
    cnt = 0
    while heap:
        if cnt == V:
            return weight
        
        now_weight,now_node = heapq.heappop(heap)

        if visited[now_node] == False:
            visited[now_node] = True
            weight += now_weight
            cnt += 1
            for next_node,next_weight in graph[now_node]:
                heapq.heappush(heap,(next_weight,next_node))



  
weight = prime()
print(weight)