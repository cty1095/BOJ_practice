import sys
from collections import deque


def bfs(bachu,visited,i,j):
    visited[i][j] = 1
    q = deque()
    q.append([i,j])   

    while q:
        u = q.popleft() 
        i = u[0]
        j = u[1]

        right = [i,j+1]
        left = [i,j-1]
        up = [i-1,j]
        down = [i+1,j]
        vector = [right,left,up,down]

        for v in vector:
            vy = v[0]
            vx = v[1]
            if 0 <=vx < len(bachu[0]) and 0 <= vy < len(bachu) :
                if visited[vy][vx] == 0 and bachu[vy][vx] ==1:
                    visited[vy][vx] = 1
                    q.append(v)

    

def cnt_worm(bachu,visited):
    cnt = 0
    for i in range(len(bachu)):
        for j in range(len(bachu[0])):
            if bachu[i][j] == 1 and visited[i][j] == 0:
                bfs(bachu,visited,i,j)
                cnt += 1
    
    return cnt



T = int(input())

for i in range(T):
    M, N, K = map(int,sys.stdin.readline().split()) #가로M, 세로N
    bachu = [[0] * (M) for _  in range(N)]
    visited = [[0] * (M) for _ in range(N)]

    for j in range(K):
        x,y = map(int,sys.stdin.readline().split())
        bachu[y][x] = 1

    worm_cnt = cnt_worm(bachu,visited)
    print(worm_cnt)
    
