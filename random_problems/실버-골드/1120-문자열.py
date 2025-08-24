import sys
input = sys.stdin.readline

A, B = input().split()

if len(A) == len(B):
    cnt = 0
    for i in range(len(A)):
        if A[i] != B[i]:
            cnt += 1
    print(cnt)

else:
    N = len(B) -len(A)
    min_cnt = len(B)
    for i in range(N+1):
        cnt = 0
        for j in range(len(A)):
            if A[j] != B[i+j]:
                cnt += 1
        min_cnt = min(cnt,min_cnt)
    print(min_cnt)

