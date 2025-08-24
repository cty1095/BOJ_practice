import sys
import math
from collections import deque
from itertools import combinations
input = sys.stdin.readline

K =1

# def lottor(K,S):
#     for comb in combinations(S,6):
#         for i in comb:
#             print(i, end=" ")
#         print()



def lottor(K,S):
    result = []
    def back(current_idx,depth):
        if depth == 6:
            print(*result)
            return
        if current_idx >= K:
            return
        result.append(S[current_idx])
        back(current_idx+1,depth+1)
        result.pop()

        back(current_idx+1,depth)

    back(0,0)

while K !=0:
    S = list(map(int,input().split()))
    K = S[0]
    S.remove(K)
    lottor(K,S)
    print()
