import sys
from collections import deque

def bfs(miro,visited):
    visited[0][0] = 1
    q = deque()
    q.append((0,0,1))
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] #상 하 좌 우

    while q:
        y, x, distance = q.popleft()

        if (y,x) ==(len(miro)-1, len(miro[0])-1):
            return distance
        
        for dy, dx in directions:
            ny = y + dy
            nx = x + dx
            if 0 <= nx < len(miro[0]) and 0 <= ny < len(miro):
                if miro[ny][nx] == 1 and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append((ny, nx, distance+1))

N, M = map(int,input().split())

miro = []
visited = [[0] * M for _ in range(N)]

for i in range(N):
    row = sys.stdin.readline().strip()
    miro.append(list(map(int, row)))

miro_distance = bfs(miro,visited)
print(miro_distance)


#miro[0][0] 과 miro[n][m]은 무조건 1임