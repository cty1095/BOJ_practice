import sys
import math
from collections import deque
from itertools import combinations
input = sys.stdin.readline

N = int(input())
listA = list(map(int,input().split()))

def NGE(listA):
    result = [-1] * N 
    stack = [0]
    for i in range(1,N):
        while stack and listA[i] > listA[stack[-1]]:
            top = stack.pop()
            result[top] = listA[i]
        stack.append(i)
        
    return result
result = NGE(listA)
print(*result)

