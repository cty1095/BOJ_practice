import heapq
import sys

def topology_sort(graph,indegree,N): #우선순위 큐 위상정렬
    heap = []
    result = []
    
    for i in range(1,N+1):
        if indegree[i] == 0:
            heapq.heappush(heap,i)


    while heap:
        now = heapq.heappop(heap)
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(heap,i)

    return result


N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for i in range(M):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1


# print(graph)
# print(indegree)

result = topology_sort(graph,indegree,N)
print(*result)