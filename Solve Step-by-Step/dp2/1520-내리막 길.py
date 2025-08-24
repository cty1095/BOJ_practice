import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

table = []

M, N = map(int,input().split())
for _ in range(M):
    row = list(map(int,input().split()))
    table.append(row)

visited = [[-1] * (N) for _ in range(M)]



def dfs(y,x):

    if (y,x) == (M-1,N-1):
        return 1

    if visited[y][x] != -1:
        return visited[y][x]


    visited[y][x] = 0
    direction = [(-1,0),(1,0),(0,-1),(0,1)]
    for next in direction:
        dy = y + next[0]
        dx = x + next[1]
        if 0 <= dy < M and 0 <= dx < N:
            if table[dy][dx] < table[y][x]:
                visited[y][x] += dfs(dy,dx)      
    
    return visited[y][x]

route=dfs(0,0)

# for row in visited:
#     print(*row)

print(route)
