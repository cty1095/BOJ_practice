import sys
input = sys.stdin.readline

def binary_search(X,Y,Z):
    left = 1
    right = 10**9
    answer = -1
    while left <= right:
        mid = (left+right)//2
        new_win_rate = ((Y + mid) * 100) // (X + mid)
        
        if new_win_rate > Z:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer

X, Y = map(int,input().split())
Z = (Y * 100) // X
if Z >= 99:
    print(-1)
else:
    min_game = binary_search(X,Y,Z)
    print(min_game)


    


