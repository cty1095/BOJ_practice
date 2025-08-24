import sys
input = sys.stdin.readline

def two_pointer(arr,N):
    X = float('inf')
    left = 0
    right = N-1
    A = 0
    B = 0
    while left < right:
        sum_LR = (arr[left] + arr[right])
        if abs(sum_LR) < X:
            X = abs(sum_LR)
            A = arr[left]
            B = arr[right]

        if sum_LR == 0:
            A = arr[left]
            B = arr[right]
            return arr[left], arr[right]
        elif sum_LR > 0:
            right -= 1
        elif sum_LR < 0:
            left += 1
    
    return A,B




N = int(input())
arr = list(map(int,input().split()))
arr.sort()
A,B = two_pointer(arr,N)
print(A,B)