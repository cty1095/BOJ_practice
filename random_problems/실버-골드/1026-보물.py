import sys
input = sys.stdin.readline

def solve(A,B,N):
    result = 0
    arr_A.sort(reverse=True)
    arr_B.sort()
    for i in range(N):
        result += arr_A[i] * arr_B[i]
    return result


N = int(input())
arr_A = list(map(int,input().split()))
arr_B = list(map(int,input().split()))
re = solve(arr_A,arr_B,N)
print(re)