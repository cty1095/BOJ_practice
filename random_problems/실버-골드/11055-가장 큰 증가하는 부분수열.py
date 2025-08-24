import sys
import math
from collections import deque
from itertools import combinations
input = sys.stdin.readline

def get_maxsum(N,listA):
    dp = [0] * N
    for i in range(N):
        dp[i] = listA[i]
    
    for i in range(N):
        max_j = 0
        for j in range(i):
            if listA[j] < listA[i]:
                max_j = max(max_j,dp[j])
        dp[i] = listA[i] + max_j

    return dp
                
            
                


N = int(input())
listA = list(map(int,input().split()))
dp = get_maxsum(N,listA)
print(max(dp))
