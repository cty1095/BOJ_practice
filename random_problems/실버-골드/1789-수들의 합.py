import sys
import math
from collections import deque
from itertools import combinations
input = sys.stdin.readline

S =int(input())


number = 0
answer = 0
while answer <= S:
    answer += number
    number += 1


print(number-2)