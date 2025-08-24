# jump는 1씩 커지고 k까지 증가했다가 다시 감소해서 1까지 내려간다.
#1 + 2+ 3 ...k + k-1 + k-2 + .... 2+ 1 이런형태의 증가햇다가 감소하는 형태
#위에 값을 다 더한 등차수열의 합 == distance

#1 + 2+ 3 ...K-1 + k + k-1 + k-2 + .... 2+ 1  -> k**2
#1 + 2+ 3 ...K-1 + k + k + k-1 + k-2 + .... 2+ 1  -> k**2 + k
#1 + 2+ 3 ...K-1 + k + k+1 + k + k-1 + k-2 + .... 2+ 1 k**2 + k + 1
import sys
import math
import heapq
from collections import deque
from itertools import combinations
input = sys.stdin.readline

def centauri(X,Y):
    distance = Y-X
    k = int(math.sqrt(distance))

    if distance <= k**2:
        return 2*k - 1
    elif distance <= k**2 + k:
        return 2*k
    else:
        return 2*k + 1

T = int(input())
for _ in range(T):
    X,Y = map(int,input().split())
    answer = centauri(X,Y)