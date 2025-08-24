# permutations 함수 

# import sys
# from itertools import permutations
# input = sys.stdin.readline

# N, M = map(int,input().split())
# list_N = list(map(int,input().split()))
# list_N.sort()

# result = permutations(list_N,M)

# for perm in result:
#     print(*perm)

# 직접 구현

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().split())
list_N = list(map(int,input().split()))
list_N.sort()

def permutation(list_N,M):
    visited = [False] * len(list_N)
    result = []
    def back():
        if len(result) == M:
            print(*result)
        
        for i in range(len(list_N)):
            if not visited[i]:
                visited[i] = True
                result.append(list_N[i])
                back()
                result.pop()
                visited[i] = False
    back()

permutation(list_N,M)




    