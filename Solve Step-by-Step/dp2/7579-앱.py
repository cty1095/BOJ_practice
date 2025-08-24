import sys
input = sys.stdin.readline

N, M = map(int,input().split()) #현재 실행중인 앱 수, 시작할 앱의 메모리

mem = list(map(int,input().split()))
costs = list(map(int,input().split()))

max_costs=sum(costs)


#dp[i][j]는 i번째 앱까지 고려했을때,  j비용으로 얻을 수 있는 최대 메모리값이다.
dp = [[0] * (max_costs+1) for _ in range(N+1)]

min_j = float('inf')

for i in range(1,N+1):
    for j in range(max_costs+1):
        if j < costs[i-1]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - costs[i-1]] + mem[i-1])
        
        if dp[i][j] >= M:
            tmp = j
            min_j = min(min_j,tmp) 


# for row in dp:
#     print(*row)


print(min_j)
