import sys
from itertools import combinations
input = sys.stdin.readline


N, S =  map(int,input().split())
arr = list(map(int,input().split()))

def solve(arr,N,S):
    cnt = 0
    def back(idx,curSum,pick):
        nonlocal cnt
        if idx == N:
            if curSum == S and pick > 0:
                cnt += 1
            return
        
        #현재원소 선택 o
        back(idx + 1, curSum + arr[idx],pick+1)
        
        #현재 원소 선택 x
        back(idx + 1, curSum,pick)

    back(0,0,0)
    return cnt

result = solve(arr,N,S)
print(result)


#itertools.combinations 사용
# def solve(arr,N,S):
#     cnt = 0
#     for i in range(1,N+1):
#         for j in combinations(arr,i):
#             if sum(j) == S:
#                 cnt += 1
#     return cnt
# result = solve(arr,N,S)
# print(result)

#문제 이해를 잘못해서 연속된 수열만 포함인줄 알고 누적합으로 구함
# prefix = [0] * (N+1)
# for i in range(1,N+1):
#     prefix[i] = prefix[i-1] + arr[i-1]
# cnt = 0
# for i in range(1,N+1):
#     for j in range(0,i):
#         if S == prefix[i]-prefix[j]:
#             cnt += 1
# print(cnt)