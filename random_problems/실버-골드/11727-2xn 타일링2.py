import sys
input = sys.stdin.readline

N = int(input())
mod = 10007
dp = [0] * (1001)
dp[1] = 1
dp[2] = 3
dp[3] = 5
dp[4] = 11
for i in range(5,N+1):
    dp[i] = ((dp[i-1] % mod) + ((dp[i-2] *2)%mod)) % mod

print(dp[N])