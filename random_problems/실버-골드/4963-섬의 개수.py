import sys
from collections import deque
input = sys.stdin.readline

def find_island(island,w,h):
    visited = [[False] * w for _ in range(h)]
    is_list = []

    def bfs(y,x):
        up =[(-1,-1),(-1,0),(-1,1)]
        mid =[(0,-1),(0,0),(0,1)] 
        down =[(1,-1),(1,0),(1,1)] 
        direction = up + mid + down
        Q = deque()
        Q.append([y,x,1])
        while Q:
            y,x,is_cnt = Q.popleft()
            for dy,dx in direction:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < h and 0 <= nx < w:
                    if visited[ny][nx] == False:
                        visited[ny][nx] = True
                        if island[ny][nx] == 1:
                            Q.append([ny,nx,is_cnt+1]) 
        return is_cnt


    for y in range(h):
        for x in range(w):
            if island[y][x] == 1 and visited[y][x] == False:
                cnt =bfs(y,x)
                is_list.append(cnt)
    return is_list



while True:
    w, h = map(int,input().split())
    if w == 0 and h == 0:
        break
    island = []
    for _ in range(h):
        row = list(map(int,input().split()))
        island.append(row)
    
    is_list = find_island(island,w,h)
    print(len(is_list))
