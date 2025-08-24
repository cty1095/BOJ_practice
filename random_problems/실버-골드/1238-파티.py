import sys
import math
import heapq
from collections import deque
from itertools import combinations
input = sys.stdin.readline

N, M, X = map(int,input().split())
graph = [[] for _ in range(N+1)]


for _ in range(M):
    start, end ,cost = map(int,input().split())
    graph[start].append((end,cost))


def round_trip(start,X):
    distance_to_X = [float('inf')] * (N+1)
    distance_to_X[start] = 0
    heap_to_X = []
    heapq.heappush(heap_to_X,(0,start))
    while heap_to_X:
        now_dist , now_city = heapq.heappop(heap_to_X)

      
        for next_city,next_dist in graph[now_city]:
            total_dist = now_dist + next_dist
            if distance_to_X[next_city] > total_dist:
                distance_to_X[next_city] = total_dist
                heapq.heappush(heap_to_X,(total_dist,next_city))
    
    #______________________________________________
    distance_to_start = [float('inf')] * (N+1)
    distance_to_start[X] = 0
    heap_to_start = []
    heapq.heappush(heap_to_start,(0,X))
    while heap_to_start:
        now_dist , now_city = heapq.heappop(heap_to_start)
        for next_city,next_dist in graph[now_city]:
            total_dist = now_dist + next_dist
            if distance_to_start[next_city] > total_dist:
                distance_to_start[next_city] = total_dist
                heapq.heappush(heap_to_start,(total_dist,next_city))

    return distance_to_X[X], distance_to_start[start]

    
max_distance = 0
for i in range(1,N+1):
    to_x,to_start = round_trip(i,X)
    # print(to_x,to_start)
    max_distance = max(to_x + to_start,max_distance)
print(max_distance)