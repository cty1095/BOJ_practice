import sys
import heapq

def dijkstra(start,graph):
    dist = [float('inf')] * (n+1)
    dist[start] = 0
    heap = []
    heapq.heappush(heap,(0,start))
    
    while heap:
        cost, now_node = heapq.heappop(heap)
        if cost > dist[now_node]:
            continue
        for next_node,next_cost in graph[now_node]:
            if dist[next_node] > cost + next_cost:
                dist[next_node] = cost + next_cost
                heapq.heappush(heap,(dist[next_node],next_node))
    return dist




T =int(input())

for i in range(T):
    n, m, t = map(int,sys.stdin.readline().split()) # 정점=6, 간선=9, 목적지후보=2
    s, g, h = map(int,sys.stdin.readline().split()) # start=2, 3-1 간선을 무조건 지나감
    graph = [[] for _ in range(n+1)]
    for j in range(m): # 간선
        a, b, d = map(int,sys.stdin.readline().split()) #a와 b 양방향, 거리=d
        graph[a].append((b,d))
        graph[b].append((a,d))
        if (a == g and b == h) or (a == h and b == g):
            gh = d

    result = []
    dist_h = dijkstra(h,graph)
    dist_s = dijkstra(s,graph)
    dist_g = dijkstra(g,graph)

    for k in range(t): # 목적지 후보
        x = int(sys.stdin.readline().strip())
        sort_load = dist_s[x]
        if sort_load == float('inf'):
            continue
        else:
            if dist_s[h] + gh + dist_g[x] == sort_load:
                result.append(x)
            elif dist_s[g] + gh + dist_h[x] == sort_load:
                result.append(x)

    result.sort()
    print(*result)