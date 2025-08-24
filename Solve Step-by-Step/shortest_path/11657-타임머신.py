import sys

def bellman_ford(start,edges,N):
    dist = [float('inf')] * (N+1)
    dist[start] = 0

    for _ in range(N-1):
        for edge in edges:
            a = edge[0]
            b = edge[1]
            c = edge[2]
            if dist[a] != float('inf') and dist[b] > dist[a] + c:
                dist[b] = dist[a] + c

    for edge in edges:
            a = edge[0]
            b = edge[1]
            c = edge[2]
            if dist[a] != float('inf') and dist[b] > dist[a] + c:
                return -1

    return dist

N, M  = map(int,input().split())
edges = []
for i in range(M):
    edge = list(map(int,sys.stdin.readline().split()))
    edges.append(edge)


dist = bellman_ford(1,edges,N)

if dist == -1:
     print(-1)
else:
    for i in range(2,N+1):
        if dist[i] == float('inf'):
            print(-1)
        else:
            print(dist[i])
