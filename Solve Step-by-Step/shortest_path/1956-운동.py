import sys

def floyd(dist):
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                
    return dist

V, E = map(int,input().split())

dist = [[float('inf')] * (V) for _ in range(V)]
for i in range(V):
    for j in range(V):
        if i == j:
            dist[i][j] = 0


for _ in range(E):
    a, b, c = map(int,sys.stdin.readline().split())
    dist[a-1][b-1] = c

dist_floyd = floyd(dist)

ans = float('inf')
for i in range(V):
    for j in range(V):
        if i != j and dist_floyd[i][j] != float('inf') and dist_floyd[j][i] != float('inf'):
            ans = min(ans, dist_floyd[i][j] + dist_floyd[j][i])

if ans == float('inf') :
    print(-1)
else:
    print(ans)

   
