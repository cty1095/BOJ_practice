import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
Deque = deque()
for _ in range(N):
    line = input().strip()
    if " " in line:
        cmd, X = line.split()
        X = int(X)
    else:
        cmd = line
    if cmd == 'push_front':
        Deque.appendleft(X)
    elif cmd == 'push_back':
        Deque.append(X)
    elif cmd == 'pop_front':
        if len(Deque) == 0:
            print(-1)
        else:
            print(Deque.popleft())
    elif cmd == 'pop_back':
        if len(Deque) == 0:
            print(-1)
        else:
            print(Deque.pop())
    elif cmd == 'size':
        size = len(Deque)
        print(size)
    elif cmd == 'empty':
        if len(Deque) == 0:
            print(1)
        else: 
            print(0)
    elif cmd == 'front':
        if len(Deque) ==0:
            print(-1)
        else:
            print(Deque[0])
    elif cmd == 'back':
        if len(Deque) ==0:
            print(-1)
        else:
            print(Deque[-1])