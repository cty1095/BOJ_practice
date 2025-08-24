import sys
input = sys.stdin.readline

N = int(input())
mod = 10007
dp = [0] * (1001)
dp[1] = 1
dp[2] = 2
dp[3] = 3
for i in range(4,N+1):
    dp[i] = ((dp[i-2] % mod) + (dp[i-1] % mod)) % mod

print(dp[N])