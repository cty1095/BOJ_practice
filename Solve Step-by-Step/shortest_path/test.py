import sys
import heapq

def dijkstra(start,end,graph):
    dist = [float('inf')] * (n+1)
    dist[start] = 0
    heap = []
    heap.append((start,0))
    
    while heap:
        now_node, cost = heapq.heappop(heap)

        if now_node == end:
            return dist[end]

        for next_node,next_cost in graph[now_node]:
            if dist[next_node] > cost + next_cost:
                dist[next_node] = cost + next_cost
                heapq.heappush(heap,(next_node,dist[next_node]))
    return dist[end]




T =int(input())
for i in range(T):
    n, m, t = map(int,sys.stdin.readline().split()) # 정점=6, 간선=9, 목적지후보=2
    s, g, h = map(int,sys.stdin.readline().split()) # start=2, 3-1 간선을 무조건 지나감
    graph = [[] for _ in range(n+1)]
    result = []
    for j in range(m): # 간선
        a, b, d = map(int,sys.stdin.readline().split()) #a와 b 양방향, 거리=d
        graph[a].append((b,d))
        graph[b].append((a,d))
    
    for k in range(t): # 목적지 후보
        x = int(sys.stdin.readline().strip())
        sort_load = dijkstra(s,x,graph) #s -> x 최단거리
        g_h = dijkstra(h,g,graph)
        if dijkstra(s,h,graph) + g_h + dijkstra(g,x,graph) == sort_load:
            result.append(x)
        elif dijkstra(s,g,graph) + g_h + dijkstra(h,x,graph) == sort_load:
            result.append(x)
    result.sort()
    print(*result)