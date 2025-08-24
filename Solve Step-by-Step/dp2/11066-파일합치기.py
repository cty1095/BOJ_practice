import sys

def solve_filesum(chapters,N):  #N = 4
    dp = [[-1] * (N+1) for _ in range(N+1)]
    prefix = [0] * (N+1)


    for i in range(1,N+1):
        dp[i][i] = 0
        prefix[i] = prefix[i-1] + chapters[i-1]

    for diagonal in range(1,N): #대각선1,2,3
        for i in range(1,N-diagonal+1):
            j = i + diagonal
            min_value = float('inf')
            for k in range(i,j):
                value = dp[i][k] + dp[k+1][j] + prefix[j] - prefix[i-1]
                if min_value > value:
                    min_value = value
            dp[i][j] = min_value

    return dp


input = sys.stdin.readline
T = int(input())
result = []

for _ in range(T):
    N = int(input())
    chapters = list(map(int,input().split()))
    dp = solve_filesum(chapters,N)
    result.append(dp[1][N])

for ans in result:
    sys.stdout.write(str(ans) + '\n')
