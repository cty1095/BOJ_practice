import sys
input = sys.stdin.readline

N ,K = map(int,input().split())
bag = []
for _ in range(N):
    weight, value = map(int,input().split())
    bag.append((weight,value))

dp = [0]*(K+1)

for weight, value in bag:
    for w in range(K, weight-1, -1):
        dp[w] = max(dp[w], dp[w-weight] + value)


print(dp)

