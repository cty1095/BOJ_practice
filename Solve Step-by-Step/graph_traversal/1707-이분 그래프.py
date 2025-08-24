import sys
from collections import deque

def bfs(graph,V):
    color = [-1] * (V+1)
    visited = [0] * (V+1)

    for i in range(1,V+1):
        if visited[i] == 0:
            q = deque()
            visited[i] = 1
            color[i] = 1 #시작 색갈은 흰색 = 1 ,  0 은 블랙이라고 가정
            q.append((i,1)) #i = 시작정점
            while q:
                point, c = q.popleft()
                for v in graph[point]:
                    if color[v] == color[point]:
                        return "NO"
                    if visited[v] == 0 and  c == 1:
                        visited[v] = 1
                        color[v] = 0
                        q.append((v,0))
                    elif visited[v] == 0 and c == 0:
                        visited[v] = 1
                        color[v] = 1
                        q.append((v,1))
    
    return "YES"



K = int(input())

for _ in range(K):
    V, E = map(int,sys.stdin.readline().split())
    graph = [[] for _ in range(V+1)]

    
    for i in range(E):
        u, v = map(int,sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    
    result = bfs(graph,V)
    print(result)