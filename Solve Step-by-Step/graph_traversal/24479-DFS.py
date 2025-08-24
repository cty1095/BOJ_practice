import sys
sys.setrecursionlimit(10**6)

N, M, R = map(int,input().split())

vertex = [i for i in range(N+1)]
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt =1

for i in range(M):
    u, v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    graph[i].sort()
    

# print(vertex)
# for edge in graph:
#     print(*edge)

def dfs(graph,R):
    global cnt
    global visited
    visited[R] = cnt

    for next in graph[R]:
        if visited[next] == 0:
            cnt += 1
            dfs(graph,next)
            
dfs(graph,R)

for i in range(1,N+1):
    print(visited[i])


