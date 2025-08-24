N = int(input())
stairs = []
for i in range(N):
    step = int(input())
    stairs.append(step)

stairs.reverse()
dp = [0  for _ in range(N)]

if N == 1:
    print(stairs[0])
elif N == 2:
    print(sum(stairs))
elif N == 3:
    ans=stairs[0] + max(stairs[1],stairs[2])
    print(ans)
else:
    dp = [0  for _ in range(N)]
    dp[0] = stairs[0]
    dp[1] = dp[0] + stairs[1]
    dp[2] = dp[0] + stairs[2]
    
    for i in range(3,N):
        dp[i] = max(dp[i-2], dp[i-3] + stairs[i-1]) + stairs[i]

    print(max(dp))
