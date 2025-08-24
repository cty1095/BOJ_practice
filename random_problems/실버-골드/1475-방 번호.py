import sys
import math
from collections import deque
input = sys.stdin.readline


number = input().strip()
counter = {}
for n in number:
    if n == '6' or n =='9':
        if '6' in counter:
            counter['6'] += 1
        else:
            counter['6'] = 1
    else:
        if n in counter:
            counter[n] += 1
        else:
            counter[n] = 1

max_set = 0
for k, v in counter.items():
    if k == '6':
        value = (counter['6'] + 1) // 2 
        max_set = max(max_set, value)
    else:
        max_set = max(max_set, v)

print(max_set)