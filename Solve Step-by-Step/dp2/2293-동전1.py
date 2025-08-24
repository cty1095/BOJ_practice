import sys
input = sys.stdin.readline

N, K = map(int,input().split())
coins = []

for _ in range(N):
    value = int(input())
    coins.append(value)

dp = [0] * (K+1)
dp[0] = 1

for coin in coins:  # 1,2,5
    for i in range(coin,K+1): #코인1일때 i의 범위 = (1,11)
        dp[i] += dp[i-coin]
        

# print(dp)
print(dp[K])