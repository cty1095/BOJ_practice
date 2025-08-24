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

def bfs(graph,i,j):
    cnt = 0
    global visited
    visited[i][j] = 1
    q = deque()  
    q.append([i,j])   

    while q:
        u = q.popleft() #graph[i][j] 처음은 i=0, j=1 
        i = u[0]
        j = u[1]
        cnt += 1

        right = [i,j+1]
        left = [i,j-1]
        up = [i-1,j]
        down = [i+1,j]
        vector = [right,left,up,down]

        for v in vector:
            vx = v[0]
            vy = v[1]
            if 0 <=vx < N  and 0 <= vy < N:
                if visited[vx][vy] == 0 and graph[vx][vy] ==1:
                    visited[vx][vy] = 1
                    q.append(v)
    return cnt

cnt_list =[]
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == 0:
            count = bfs(graph,i,j)
            cnt_list.append(count)

print(len(cnt_list))
for c in sorted(cnt_list):
    print(c)



