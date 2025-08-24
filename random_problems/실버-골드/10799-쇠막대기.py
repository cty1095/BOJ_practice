import sys
import math
from collections import deque
input = sys.stdin.readline

stack = []
result = 0

A = input().strip()
B=A.replace('()','R')

for letter in B:
    if letter == '(':
        stack.append(letter)
    elif letter == "R":
        result += len(stack)
    elif letter == ')':
        stack.pop()
        result += 1

print(result)


