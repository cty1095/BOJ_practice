import sys

def floyd(dist):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])

    return dist


N = int(input())
M = int(input())

dist = [[float('inf')] * (N) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            dist[i][j] = 0

for _ in range(M):
    a, b, c = map(int,sys.stdin.readline().split())
    dist[a-1][b-1] = min(dist[a-1][b-1],c)

result = floyd(dist)


for i in range(N):
    for j in range(N):
        if result[i][j] == float('inf'):
            result[i][j] = 0


for row in result:
    print(*row)