import sys
input = sys.stdin.readline

def two_pointer(prefix, N, S):
    left = 0
    right = 0
    lenth = []
    while right <= N:
        if prefix[right] - prefix[left] >= S:
            tmp = right-left
            lenth.append(tmp)
            left += 1
        elif prefix[right] - prefix[left] < S:
            right += 1
    if len(lenth) == 0:
        return 0
    else:
        return min(lenth)

N, S = map(int,input().split())
prefix = [0] * (N+1)
arr = list(map(int,input().split()))

for i in range(1,N+1):
    prefix[i] = prefix[i-1] + arr[i-1]
# print(prefix)

re = two_pointer(prefix,N,S)
print(re)
