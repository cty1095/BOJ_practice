import sys
input = sys.stdin.readline

def dp(stickers,N):
    if N == 1:
        return max(stickers[0][0],stickers[1][0])
    elif N >= 2:

        table = [[0] * N for _ in range(2)]
        table[0][0] = stickers[0][0]
        table[1][0] = stickers[1][0]
        
        table[0][1] = table[1][0] + stickers[0][1]
        table[1][1] = table[0][0] + stickers [1][1]
        for x in range(2,N):
            table[0][x] = stickers[0][x] + max(table[1][x-1],table[1][x-2])
            table[1][x] = stickers[1][x] + max(table[0][x-1],table[0][x-2])
        
        answer  = max(table[0][N-1],table[1][N-1])
        return answer


T = int(input())
for _ in range(T):

    N = int(input())

    visited = [[False] * N for _ in range(2)]
    stickers = []

    for i in range(2):
        row = list(map(int,input().split()))
        stickers.append(row)
    ans = dp(stickers,N)
    print(ans)
