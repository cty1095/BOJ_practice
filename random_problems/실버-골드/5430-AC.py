import sys
import math
from collections import deque
from itertools import combinations
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    error = False
    revers = False
    cmd = input().strip()
    N = int(input())
    if N == 0:
        s = input().strip()
        Q = deque()
    else:
        s = input().strip()
        s = s.strip('[]')  
        Q = deque(s.split(','))
    for command in cmd:
        if command == "R":
            if len(Q) == 0:
                continue
            else:
                revers = not revers

        elif command == "D":
            if len(Q) == 0:
                error = True
            else:
                if revers == True:
                    Q.pop()
                elif revers == False:
                    Q.popleft()
    if error == True:
        print('error')     
    else:
        if revers == True:
            Q.reverse()
        print('[' + ','.join(Q) + ']')
