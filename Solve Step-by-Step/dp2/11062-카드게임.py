import sys
input = sys.stdin.readline

def pick_cards(cards,N):
    dp = [[0] *(N) for _ in range(N)]
    prefix = [0] *(N+1)
    for i in range(1,N+1):
        prefix[i] = prefix[i-1] + cards[i-1]
    
    for length in range(1,N+1):
        for left in range(0,N-length+1):
            right = left + length -1
            if left == right:
                dp[left][right] = cards[left]
            else:
                left_pick = cards[left] + prefix[right+1] - prefix[left+1] -dp[left+1][right]
                right_pick = cards[right] + prefix[right] - prefix[left] -dp[left][right-1]
                dp[left][right] = max(left_pick,right_pick)
    return dp
T = int(input())
for _ in range(T):
    N = int(input())
    cards = list(map(int,input().split()))
    dp = (pick_cards(cards,N))
    # for row in dp:
    #     print(*row)
    print(dp[0][N-1])
        

    