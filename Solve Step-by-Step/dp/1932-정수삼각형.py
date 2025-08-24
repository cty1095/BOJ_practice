N= int(input())
triangle = []
for _ in range(N):
    row = list(map(int,input().split()))
    triangle.append(row)

dp = [[0] * (i + 1) for i in range(N)]
dp[0][0] = triangle[0][0]
for i in range(1,N):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][0] + triangle[i][0]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + triangle[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + triangle[i][j]

# for row in dp:
#     print(*row)

print(max(dp[N-1]))