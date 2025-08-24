import sys
import math
from collections import deque
from itertools import combinations
input = sys.stdin.readline



N = int(input())
mod = 10007
dp = [[1] * 10 for _ in range(1001)]


for i in range(2,1001):
    for j in range(10):
        if j > 0 :

            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % mod
        else:
            dp[i][j] = 1

print(sum(dp[N]) % mod)