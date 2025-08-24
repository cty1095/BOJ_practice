from collections import deque

visited = [0] * (10**5+1)
N, K = map(int,input().split())

def bfs(N,K,distance):
    global visited
    visited[N] = 1
    q = deque()
    q.append((N,distance))
    
    while q:
        x, distance = q.popleft()
        if x == K:
            return distance
        direction = [x-1,x+1,2*x]
        for nx in direction:
            if 0 <= (nx) < len(visited) and visited[nx] != 1:
                visited[nx] = 1
                q.append((nx,distance+1))

dis = bfs(N,K,0)    
print(dis)