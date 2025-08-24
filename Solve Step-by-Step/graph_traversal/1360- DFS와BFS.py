import sys
from collections import deque
sys.setrecursionlimit(10**6)

N, M, R = map(int,input().split())

graph = [[] for _ in range(N+1)]
visited_DFS = []
visited_BFS = []

for i in range(M):
    u, v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    graph[i].sort()
    

# print(vertex)
# for row in graph:
#     print(*row)

def dfs(graph,R):
    global visited_DFS
    visited_DFS.append(R)

    for next in graph[R]:
        if next not in visited_DFS:
            dfs(graph,next)



def bfs(graph,R):
    global visited_BFS
    visited_BFS.append(R)
    q = deque()  
    q.append(R)   

    while q:
        u = q.popleft()
        for next in graph[u]:
            if next not in visited_BFS:
                visited_BFS.append(next)
                q.append(next)


dfs(graph,R)
bfs(graph,R)     

print(*visited_DFS)
print(*visited_BFS)



