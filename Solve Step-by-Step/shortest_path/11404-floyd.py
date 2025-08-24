import sys

N = int(sys.stdin.readline())
m = int(sys.stdin.readline())

INF = int(1e9)
city = [([INF]*N) for _ in range(N)]

for i in range(N):
    city[i][i] = 0


for _ in range(m):
    i, j, cost = map(int,input().split())
    # city[i-1][j-1] = cost
    if city[i-1][j-1] >= cost:
        city[i-1][j-1] = cost

def floyd(w,N):
    dp = w
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    return dp

# print("init : ", city)
# print('-------------')
dp = floyd(city,N)

for i in range(N):
    for j in range(N):
        if dp[i][j] == INF:
            dp[i][j] = 0            #갈수 없는 경우 0으로 
# print("final :" , *dp)


for row in dp:
    print(*row)
