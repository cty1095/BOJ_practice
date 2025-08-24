strA = input()
strB = input()
A = len(strA)
B = len(strB)


dp = [[0] * (B+1) for _ in range(A+1)]

for i in range(1,A+1):
    for j in range(1,B+1):
        if strA[i-1] == strB[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

print(dp[A][B])