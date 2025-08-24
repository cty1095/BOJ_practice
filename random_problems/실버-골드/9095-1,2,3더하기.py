import sys
input = sys.stdin.readline

def sum_123():
    dp = [0] * (13)
    dp[1] = 1 # 1
    dp[2] = 2 # 1+1, 2
    dp[3] = 4 # 1+1+1, 1+2, 2+2, 3
    for i in range(4,12):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    
    return dp

T =int(input())

result = sum_123()
for _ in range(T):
    N = int(input())
    print(result[N])