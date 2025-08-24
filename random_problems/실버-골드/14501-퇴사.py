import sys
input = sys.stdin.readline

N = int(input())
event = []
for _ in range(N):
    T, P = map(int,input().split())
    event.append([T,P])
dp = [0] * (N+1) 
for i in range(N):
    T,P = event[i]
    end_day = i+T
    if end_day <= N:
        dp[end_day] = max(dp[end_day],dp[i]+P)
    dp[i + 1] = max(dp[i + 1], dp[i])

print(dp[N])