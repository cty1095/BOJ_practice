import sys
import math
from collections import deque
from itertools import combinations
input = sys.stdin.readline

def find_region(color):
    visited = [[False] * N for _ in range(N)]
    def bfs(y,x,C):
        Q = deque()
        visited[y][x] = True
        direction = [(-1,0),(1,0),(0,-1),(0,1)]
        Q.append([y,x,C])
        while Q:
            y,x,C = Q.popleft()
            for dy,dx in direction:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < N and 0 <= nx < N:
                    if visited[ny][nx] == False and color[ny][nx] == C:
                        visited[ny][nx] = True
                        Q.append([ny,nx,C])
        return 1
    
    cnt = 0

    for y in range(N):
        for x in range(N):
            if visited[y][x] == False:
                C = color[y][x]
                cnt += bfs(y,x,C)

    return cnt

def fine_weak_region(color):
    visited = [[False] * N for _ in range(N)]
    # for y in range(N):
    #     for x in range(N):
    #         if color[y][x] == 'G':
    #             color[y][x] = 'R'
    #-------------------------------------
    def bfs(y,x,C):
        Q = deque()
        visited[y][x] = True
        direction = [(-1,0),(1,0),(0,-1),(0,1)]
        Q.append([y,x,C])
        while Q:
            y,x,C = Q.popleft()
            for dy,dx in direction:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < N and 0 <= nx < N:
                    if visited[ny][nx] == False:
                        if C =='R' or C=='G':
                            if color[ny][nx] == 'R' or color[ny][nx] == 'G':
                                visited[ny][nx] = True
                                Q.append([ny,nx,C])
                        elif C == 'B':
                           if color[ny][nx] == C:
                            visited[ny][nx] = True
                            Q.append([ny,nx,C])
        return 1
    
    cnt = 0

    for y in range(N):
        for x in range(N):
            if visited[y][x] == False:
                C = color[y][x]
                cnt += bfs(y,x,C)

    return cnt


N = int(input())

color = []
for _ in range(N):
    row = input().strip()
    color.append(row)

region = find_region(color)
weak_region=fine_weak_region(color)

print(region,weak_region)
