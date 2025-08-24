import sys
from collections import deque
input = sys.stdin.readline

N, M, K, start = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(M):
    A, B = map(int,input().split())
    graph[A].append(B)

#다익스트라 아니면 bfs 둘중에 하나같은데
#일단 bfs로 풀어보자 why? 모든 도로의 길이가 1임

def bfs(graph,start,K):
    global visited
    city = []
    Q = deque()
    Q.append([start,0])
    visited[start] = True
    while Q:
        node,distance = Q.popleft()
        if distance == K:
            city.append(node)
        for next in graph[node]:
            if visited[next] == False:
                visited[next] = True
                Q.append([next,distance+1])
            
    if len(city) == 0:
        print(-1)
    else:
        city.sort()
        for i in city:
            print(i)   

bfs(graph,start,K)