import sys
import math
import heapq
from collections import deque
from itertools import combinations
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
distance = [float('inf')] * (N+1)


for _ in range(M):
    start, end, cost = map(int,input().split())
    graph[start].append((end,cost))

X,Y = map(int,input().split())
distance[X] = 0

def dis(X,Y):
    global distance
    heap =  []
    heapq.heappush(heap,(0,X))

    while heap:
        now_dis, now_node = heapq.heappop(heap)
        
        if distance[now_node] < now_dis:
            continue

        for next_node, next_dis in graph[now_node]:
            if distance[next_node] > next_dis+now_dis:
                distance[next_node] = next_dis+now_dis
                heapq.heappush(heap,(next_dis+now_dis,next_node))
    return distance[Y]

answer = dis(X,Y)
print(answer)
