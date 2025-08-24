import sys
import math
from collections import deque
from itertools import combinations
input = sys.stdin.readline

def fill_field(x1,y1,x2,y2):
    global field
    for y in range(y1,y2):
        for x in range(x1,x2):
            field[y][x] += 1

def search_zero(y,x):
    global visited
    Q = deque()
    direction = [(-1,0),(1,0),(0,-1),(0,1)] #상하좌우
    Q.append([y,x])
    cnt = 1
    while Q:
        y,x = Q.popleft()
        for dy,dx in direction:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < M and 0<= nx < N:
                if visited[ny][nx] == False and field[ny][nx] == 0:
                    visited[ny][nx] = True
                    cnt += 1
                    Q.append([ny,nx])

    return cnt



M,N,K = map(int,input().split())
field = [[0] * N for _ in range(M)]
visited = [[False] * N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int,input().split())
    fill_field(x1,y1,x2,y2)

result = []
for y in range(M):
    for x in range(N):
        if field[y][x] == 0 and visited[y][x] == False:
            visited[y][x] = True
            cnt =search_zero(y,x)
            result.append(cnt)


result.sort()
print(len(result))
print(*result) 

# for row in field:
#     print(*row)

# for row in visited:
#     print(*row)