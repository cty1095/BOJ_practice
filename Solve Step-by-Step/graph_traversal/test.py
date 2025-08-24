V, E = map(int,input().split())
graph = [[] for _ in range(V+1)]

    
for i in range(E):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

print(graph)