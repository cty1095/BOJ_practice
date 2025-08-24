import sys
from collections import deque
input = sys.stdin.readline

def serach_safezone(region,max_height):
    def bfs(y,x,water_height):
        Q = deque()
        visited[y][x] = True
        direction = [(-1,0),(1,0),(0,-1),(0,1)] #상하좌우가운데
        Q.append([y,x,1])
        while Q:
            y,x,cnt = Q.popleft()
            for dy,dx in direction:
                ny = y + dy
                nx = x + dx
                if 0<= ny < N and 0<= nx < N:
                    if region[ny][nx] >= water_height and visited[ny][nx] == False:
                        visited[ny][nx] =True
                        Q.append([ny,nx,cnt+1])


        return cnt
    
    max_safety_zone = 0
    
    for i in range(max_height+1):
        safe_zone = 0
        visited = [([False] * N) for _ in range(N)]
        for y in range(N):
            for x in range(N):
                if region[y][x] >= i and visited[y][x] == False:
                    bfs(y,x,i)
                    safe_zone += 1
        max_safety_zone = max(max_safety_zone,safe_zone)

    return max_safety_zone


region = []
N =int(input())
max_height = 0


for _ in range(N):
    row = list(map(int,input().split()))
    height = max(row)
    max_height = max(max_height,height)
    region.append(row)

answer = serach_safezone(region,max_height)
print(answer)
