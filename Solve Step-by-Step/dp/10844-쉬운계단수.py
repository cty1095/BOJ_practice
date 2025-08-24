N = int(input())

dp = [[0] * 11 for i in range(N+1)]

for k in range(1,10):
    dp[1][k] = 1

for i in range(2,N+1):
    for j in range(10):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

# for row in dp:
#     print(*row)

# print("--------------")

ans = (sum(dp[N])) % 1000000000
print(ans)