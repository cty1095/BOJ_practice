import sys 
input = sys.stdin.readline

def fivo(dp):
    for i in range(2,41):
        dp[i][0] = dp[i-1][0] + dp[i-2][0]
        dp[i][1] = dp[i-1][1] + dp[i-2][1]
    return dp

T = int(input())
dp = [[0,0] for _ in range(41)]
dp[0] = [1,0]
dp[1] = [0,1]
fivo(dp)

for _ in range(T):
    N = int(input())
    ans=dp[N]
    print(*ans)