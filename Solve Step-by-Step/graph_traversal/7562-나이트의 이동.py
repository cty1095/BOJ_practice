from collections import deque
import sys


def bfs(x,y,g_x,g_y,visited):
    visited[x][y] = 1
    q = deque()
    q.append((x,y,0))
    
    while q:
        x,y,distance = q.popleft()
        if (x,y) == (g_x,g_y):
            return distance
        direction = [(x-2,y-1),(x-1,y-2),(x+1,y-2),(x+2,y-1),(x+2,y+1),(x+1,y+2),(x-1,y+2),(x-2,y+1)]
        for move in direction:
            nx = move[0]
            ny = move[1]
            if 0 <= nx < len(visited) and 0 <= ny < len(visited):
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx,ny,distance+1))

T = int(input())
for i in range(T):
    I = int(input())
    visited = [[0] * I for _ in range(I)]
    x,y = map(int,sys.stdin.readline().split())
    goal_x,goal_y =map(int,sys.stdin.readline().split())
    dis =bfs(x,y,goal_x,goal_y,visited)
    print(dis)