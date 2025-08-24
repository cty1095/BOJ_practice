N = int(input())
listA = list(map(int,input().split()))

dp = [1] * N
for i in range(1,N):
    for j in range(0,i):
        if listA[j] < listA[i]:
            dp[i] = max(dp[i],dp[j]+1)
# print(dp)
# print(max(dp))
# print("-------------")

dwn_dp = [1] * N
listB = listA[::-1]

for i in range(1,N):
    for j in range(0,i):
        if listB[j] < listB[i]:
            dwn_dp[i] = max(dwn_dp[i],dwn_dp[j]+1)

dwn_dp.reverse()


ans = 0
for i in range(N):
    tmp = dp[i] + dwn_dp[i] -1
    if ans < tmp:
        ans = tmp

print(ans)