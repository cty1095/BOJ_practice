import sys
import math
from collections import deque
from itertools import combinations
input = sys.stdin.readline

N =int(input())
list_P = list(map(int,input().split()))
list_P.insert(0,0)
dp = [0] * (N+1) 
dp[1] = list_P[1]

for i in range(2,N+1): #카드 i개를 갖기 위해 지불해야하는 최댓값
    for j in range(1,i+1):
        dp[i] = max(dp[i-j] + list_P[j],dp[i])
   
print(dp[N])

