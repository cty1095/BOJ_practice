import sys
input = sys.stdin.readline

N, M = map(int,input().split())

num = list(map(int,input().split()))

prefix = [0] * (N+1)

for i in range(1,N+1):
    prefix[i] = prefix[i-1] + num[i-1]

# print(prefix)

for i in range(M):
    start, end = map(int,input().split())
    ans = prefix[end] - prefix[start-1]
    print(ans)