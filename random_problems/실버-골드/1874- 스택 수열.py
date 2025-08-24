import sys
import math
input = sys.stdin.readline

T = int(input())
stack = [0]
result = []
trash = []
mem = 1
sequence = True

for _ in range(T):
    N = int(input())
    while mem <= N:
        stack.append(mem)
        mem += 1
        result.append('+')
    if stack[-1] == N:
        stack.pop()
        result.append('-')
    else:
        sequence = False
        break
    
if sequence == False:
    print('NO')
else:
    for plus in result:
        print(plus)
