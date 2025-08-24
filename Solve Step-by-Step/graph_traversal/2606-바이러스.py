from collections import deque
import sys
sys.setrecursionlimit(10**6)

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = []

for i in range(M):
    u, v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    graph[i].sort()
    

# for edge in graph:
#     print(*edge)

def bfs(graph,R):
    global visited
    visited.append(R)
    q = deque()  
    q.append(R)   

    while q:
        u = q.popleft()
        for next in graph[u]:
            if next not in visited:
                visited.append(next)
                q.append(next)
            
bfs(graph,1)
print(len(visited)-1)



