import sys
import math
from collections import deque
input = sys.stdin.readline

stack_left = []
stack_right = []
string = input().strip()
for ch in string:
    stack_left.append(ch)

M = int(input())

for _ in range(M):
    cmd = input().split()
    if cmd[0] == 'L':
        if len(stack_left) == 0:
            continue
        else:
            A=stack_left.pop()
            stack_right.append(A)
    elif cmd[0] == 'D':
        if len(stack_right) == 0:
            continue
        else:      
            A=stack_right.pop()
            stack_left.append(A)

    elif cmd[0] == 'B':
        if len(stack_left) == 0:
            continue
        else:
            stack_left.pop()
    elif cmd[0] == 'P':
        stack_left.append(cmd[1])
        
result = stack_left + stack_right[::-1]

print(''.join(result))