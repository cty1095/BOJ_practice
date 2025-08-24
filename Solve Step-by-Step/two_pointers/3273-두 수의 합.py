import sys

def two_pointer(arr,N,X):
    left = 0
    right = N-1
    cnt = 0
    while left < right:
        if arr[left] + arr[right] == X:
            cnt += 1
            left += 1
            right -= 1
        elif arr[left] + arr[right] > X:
            right -= 1
        elif arr[left] + arr[right] < X:
            left += 1
    return cnt

N = int(input())
arr = list(map(int,sys.stdin.readline().split()))
arr.sort()
X = int(input())
re =two_pointer(arr,N,X)
print(re)