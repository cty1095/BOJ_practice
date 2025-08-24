import sys
from collections import deque

def toma(tomato,H,N,M):
    zero_cnt = 0
    q = deque()
    max_day = 0
    day = 0
    direction = [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]
    for h in range(H):
        for y in range(N):
            for x in range(M):
                if tomato[h][y][x] == 1:
                    q.append((h,y,x,day))
                elif tomato[h][y][x] == 0:
                    zero_cnt += 1
    while q:
        h,y,x,day = q.popleft()
        max_day = max(max_day, day)
        for move in direction:
            nh = h + move[0]
            ny = y + move[1]
            nx = x + move[2]
            if 0 <= nh < H and 0 <= ny < N and 0 <= nx < M:
                if tomato[nh][ny][nx] == 0:
                    tomato[nh][ny][nx] = 1
                    q.append((nh,ny,nx,day+1))
                    zero_cnt -= 1

    if zero_cnt == 0:
        return max_day
    else:
        return -1

M,N,H = map(int,input().split())
tomato = []

for i in range(H):
    tomato_H = []
    for j in range(N):
        row = list(map(int,sys.stdin.readline().split()))
        tomato_H.append(row)
    tomato.append(tomato_H)


mxday= toma(tomato,H,N,M)
print(mxday)

