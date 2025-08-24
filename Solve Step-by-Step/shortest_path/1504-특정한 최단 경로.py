import heapq
import sys

def dijkstra(start,end):
    global graph
    dist = [float('inf')] * (N+1)
    dist[start] = 0
    heap = []
    heapq.heappush(heap,(0,start))

    while heap:
        now_dist, now_node = heapq.heappop(heap)
        
        for next in graph[now_node]:
            next_node = next[0]
            next_cost = next[1]
            if dist[next_node] > now_dist + next_cost:
                dist[next_node] = now_dist + next_cost
                heapq.heappush(heap,(dist[next_node],next_node))
    return dist[end]


N, E = map(int,input().split())

graph = [[] for _ in range(N+1)]
for i in range(E):
    a, b, c = map(int,sys.stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1, v2 = map(int,input().split())

#start -> v1 - > v2 - > end
load1 = dijkstra(1,v1) + dijkstra(v1,v2) + dijkstra(v2,N)
#start -> v2 -> v1 -> end
load2 = dijkstra(1,v2) + dijkstra(v2,v1) + dijkstra(v1,N)

if load1 == float('inf') and load2 == float('inf'):
    print(-1)
else:
    print(min(load1,load2))

