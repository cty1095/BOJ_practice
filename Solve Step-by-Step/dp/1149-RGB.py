N = int(input())
cost = []
for i in range(N):
    row = list(map(int,input().split()))
    cost.append(row)

def solve(N,cost):
    dp = [([0] * 3)for _ in range(N)]
    for i in range(3):
        dp[0][i] = cost[0][i]
    
    for i in range(1,N):
        dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + cost[i][0]
        dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + cost[i][1]
        dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + cost[i][2]
        


    ans = min(dp[N-1][0],dp[N-1][1],dp[N-1][2])
    
    return dp,ans



dp,ans = solve(N,cost)
# print("-------------")

# for row in dp:
#     print(*row)

print(ans)

