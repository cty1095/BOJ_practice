import sys
import math
from collections import deque
from itertools import combinations
input = sys.stdin.readline

T =int(input())

for _ in range(T):
    N = int(input())
    clothes_dic = {}
    answer = 1
    for _ in range(N):
        item, category = input().split()
        if category in clothes_dic:
            clothes_dic[category].append(item)
        else:
            clothes_dic[category] = [item]
   
    for k,v in clothes_dic.items():
        multiple = len(clothes_dic[k]) + 1
        if multiple == 0:
            continue
        else:
            answer *= multiple
    print(answer-1)
