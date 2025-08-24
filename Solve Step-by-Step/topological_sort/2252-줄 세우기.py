import sys
from collections import deque

N, M = map(int,input().split())
indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
q = deque()
for i in range(M):
    A, B = map(int,sys.stdin.readline().split())
    graph[A].append(B)
    indegree[B] += 1

def topology_sort(indegree,graph,N):
    q = deque()
    result = []
    
    for i in range(1,N+1):  #차수 0 이면 큐에 추가
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    return result

result = topology_sort(indegree,graph,N)
print(*result)