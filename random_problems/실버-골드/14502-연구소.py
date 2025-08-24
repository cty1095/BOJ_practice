import sys
import math
from collections import deque
from itertools import combinations
input = sys.stdin.readline

def get_max_safezone(field,N,M):
    max_safezone = 0
    empties = []
    for y in range(N):
        for x in range(M):
            if field[y][x] == 0:
                empties.append((y,x))
                


    def backtracking(start,wall):
        nonlocal max_safezone

        if wall == 3:
            temp = [row[:] for row in field] 
            spread_virus(temp)
            safezone = counting_zero(temp)
            max_safezone = max(max_safezone,safezone)
            return
        
        for i in range(start,len(empties)):
            y,x = empties[i]
            field[y][x] = 1
            backtracking(i+1,wall+1)
            field[y][x] = 0



    def spread_virus(field):
        visited = [[False] * M for _ in range(N)]

        def bfs(y,x):
            Q = deque()
            visited[y][x] = True
            Q.append([y,x])
            direction = [(-1,0),(1,0),(0,-1),(0,1)]
            while Q:
                y,x = Q.popleft()
                for dy,dx in direction:
                    ny = dy + y
                    nx = dx + x
                    if 0 <= ny < N and 0 <= nx < M:
                        if field[ny][nx] == 0 and visited[ny][nx] == False:
                            field[ny][nx] = 2
                            visited[ny][nx] =True
                            Q.append([ny,nx])
        for y in range(N):
            for x in range(M):
                if field[y][x] == 2:
                    bfs(y,x)

        return field
    def counting_zero(field):
        zero = 0
        for i in range(N):
            zero += field[i].count(0)
        return zero
    
    backtracking(0,0)
    return max_safezone




N,M = map(int,input().split())
field = []

for _ in range(N):
    row = list(map(int,input().split()))
    field.append(row)



safezone = get_max_safezone(field,N,M)
print(safezone)
