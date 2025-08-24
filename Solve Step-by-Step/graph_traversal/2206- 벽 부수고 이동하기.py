import sys
from collections import deque

def bfs(board,visited,N,M):
    visited[0][0][0] = 1
    direction = [(-1,0),(1,0),(0,-1),(0,1)] #상 하 좌 우
    q = deque()
    q.append((0,0,1,0)) #y,x,cnt,break=0 안부숨, =1 부숨
    while q:
        y,x,cnt,wall_break = q.popleft()
        if (y,x) == (N-1,M-1):
            return cnt
        for move in direction:
            ny = y + move[0]
            nx = x + move[1]
            if 0 <= ny < N and 0 <= nx < M:
                if visited[ny][nx][wall_break] == 0 and board[ny][nx] == 0:
                    visited[ny][nx][wall_break] = 1
                    q.append((ny,nx,cnt+1,wall_break))

                elif visited[ny][nx][wall_break] == 0 and board[ny][nx] == 1:
                    if wall_break == 0:
                        visited[ny][nx][1] = 1
                        q.append((ny,nx,cnt+1,1))
                        

N, M = map(int,input().split())

board = []
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
for _ in range(N):
    row = list(map(int, sys.stdin.readline().strip()))
    board.append(row)

result = bfs(board,visited,N,M)
if result != None:
    print(result)
else:
    print(-1)

