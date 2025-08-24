N = int(input())
listA = list(map(int,input().split()))

dp = [1 for _ in range(N)]
for i in range(1,N):
    for j in range(0,i):
        if listA[j] < listA[i]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))