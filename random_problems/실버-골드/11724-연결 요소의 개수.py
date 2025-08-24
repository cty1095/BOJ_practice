import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph,start):
    global visited
    Q = deque()
    Q.append([start,1])
    while Q:
        node,cnt = Q.popleft()
        for next in graph[node]:
            if visited[next] == False:
                visited[next] = True
                Q.append([next,cnt+1])
    return cnt


N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(M):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
cnt_lst = []

for i in range(1,N+1):
    if visited[i] == False:
        cnt = bfs(graph,i)
        cnt_lst.append(cnt)
print(len(cnt_lst))

