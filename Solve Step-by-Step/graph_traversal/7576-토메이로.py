import sys
from collections import deque

def toma(tomato,visited,N,M):
    q = deque()
    max_day = 0
    day = 0
    direction = [(-1,0),(1,0),(0,-1),(0,1)]
    for y in range(N):
        for x in range(M):
            if tomato[y][x] == 1 and visited[y][x] == 0:
                q.append((x,y,day))
                visited[y][x] = 1
    while q:
        x,y,day = q.popleft()
        max_day = max(max_day, day)
        for move in direction:
            ny = y + move[0]
            nx = x + move[1]
            if 0 <= ny < N and 0 <= nx < M:
                if visited[ny][nx] == 0 and tomato[ny][nx] != -1:
                    visited[ny][nx] = 1
                    if tomato[ny][nx] ==0:
                        tomato[ny][nx] = 1
                    q.append((nx,ny,day+1))
    return max_day

M,N = map(int,input().split())
tomato = []
visited = [[0] * M for _ in range(N)]

for i in range(N):
    row = list(map(int,sys.stdin.readline().split()))
    tomato.append(row)

day = toma(tomato,visited,N,M)
flag = True
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 0:
            flag = False 
            break
if flag:
    print(day)
else:
    print(-1)


