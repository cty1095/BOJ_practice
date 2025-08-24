N , K = map(int,input().split())
items = []
for i in range(N):
    item = list(map(int,input().split())) # weight, value
    items.append(item)

dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,K+1):
        if items[i-1][0] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - items[i-1][0]] + items[i-1][1])

print(dp[N][K])


# print("-------------")
# for row in items:
#     print(*row)
# print("--------------")
# for row in dp:
#     print(*row)