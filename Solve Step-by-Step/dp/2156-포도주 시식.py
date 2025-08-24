N = int(input())
podoju_sum = []
for i in range(N):
    podoju = int(input())
    podoju_sum.append(podoju)

if N == 1:
    print(podoju_sum[0])
elif N == 2:
    print(podoju_sum[0] + podoju_sum[1])
else:
    dp = [0  for _ in range(N)]
    dp[0] = podoju_sum[0]
    dp[1] = dp[0] + podoju_sum[1]
    dp[2] = max((podoju_sum[0]+podoju_sum[1]),(podoju_sum[0]+podoju_sum[2]),(podoju_sum[1]+podoju_sum[2]))
    
    for i in range(3,N):
        dp[i] = max(dp[i-1],dp[i-2]+podoju_sum[i],dp[i-3]+podoju_sum[i-1]+podoju_sum[i])

    print(max(dp))
