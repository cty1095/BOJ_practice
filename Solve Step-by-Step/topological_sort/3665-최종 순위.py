from collections import deque
import sys

def topology_sort(indegree,graph,N):
    q = deque()
    result = []
    indegree = indegree[:] 
    
    for i in range(1,N+1):  
        if indegree[i] == 0:
            q.append(i)

    while q:
        if len(q) >= 2:
            return "?"
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    if len(result) < N:
        return "IMPOSSIBLE"

    return result

T = int(input())
for i in range(T):
    n = int(input())
    last_year = list(map(int,sys.stdin.readline().split()))
    last_graph = [[] for _ in range(n+1)]
    last_indegree = [0] * (n+1)

    for j in range(n):
        for k in range(j+1,n):
            a,b = last_year[j], last_year[k]
            last_graph[a].append(b)
            last_indegree[b] += 1

    # print("작년 graph : " , last_graph)
    # print("작년 indegree : " , last_indegree)

    m = int(input())
    
    for j in range(m):
        a, b = map(int,sys.stdin.readline().split())  #올해 a -> b 역전 
        if a in last_graph[b]:                        #작년 b -> a 상황
            last_graph[b].remove(a)
            last_graph[a].append(b)  
            last_indegree[a] -= 1
            last_indegree[b] += 1

        elif b in last_graph[a]:
            last_graph[a].remove(b)
            last_graph[b].append(a)  
            last_indegree[b] -= 1
            last_indegree[a] += 1


    # print("올해 graph : " , last_graph)
    # print("올해 indegree : " , last_indegree)

    result = topology_sort(last_indegree,last_graph,n)
    if result == "IMPOSSIBLE":
        print("IMPOSSIBLE")
    elif result == "?":
        print("?")
    else:
        print(*result)


