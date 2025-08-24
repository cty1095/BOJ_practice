N = int(input())
wire = []

for i in range(N):
    row = list(map(int,input().split()))
    wire.append(row)


# print(wire)
# print("-----------")
wire.sort()
# print(wire)


dp = [1 for _ in range(N)]
for i in range(1,N):
    for j in range(0,i):
        if wire[j][1] < wire[i][1]:
            dp[i] = max(dp[i],dp[j]+1)
# print(dp)

print(N - max(dp))

