from collections import deque
import sys
sys.setrecursionlimit(10**6)

N = int(input())
visited = [[0] * (N) for _ in range(N)]
graph = []

for i in range(N):
    row = list(map(int,sys.stdin.readline().strip()))
    graph.append(row)    

# for row in graph:
#     print(*row)

def DFS(graph,i,j):
    cnt = 0
    pass
    return cnt


cnt_list =[]
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == 0:
            count = DFS(graph,i,j)
            cnt_list.append(count)

print(len(cnt_list))
for c in sorted(cnt_list):
    print(c)



