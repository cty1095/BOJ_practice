import sys
import heapq


V, E = map(int,input().split())  #정점개수, 간선개수
K = int(input())  #시작 정점

dist = [float('inf')] * (V+1)
dist[K] = 0

graph = [[] for _ in range(V+1)]

# print(dist)

for i in range(E):
    u, v, w = map(int,sys.stdin.readline().split())
    graph[u].append((v, w))

heap = []

heapq.heappush(heap,(0,K))

while heap:
    now_dist,now_node = heapq.heappop(heap)
    
    if now_dist > dist[now_node]:
        continue 
    
    for next in graph[now_node]:
        next_V = next[0]
        cost_V = next[1]

        if dist[next_V] > now_dist + cost_V:
            dist[next_V] = now_dist + cost_V
            heapq.heappush(heap,(dist[next_V],next_V))


for i in range(1,V+1):
    if dist[i] == float('inf'):
        print("INF")
    else:
        print(dist[i])