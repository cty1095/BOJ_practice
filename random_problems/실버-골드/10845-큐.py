import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
Q = deque()

for _ in range(N):
    cmd = input().split()
    if cmd[0] == 'push':
        Q.append(int(cmd[1]))

    elif cmd[0] == 'pop':
        if len(Q) == 0:
            print(-1)
        else:
            print(Q.popleft())
    
    elif cmd[0] == 'size':
        print(len(Q))
    
    elif cmd[0] == 'empty':
        if len(Q) == 0:
            print(1)
        else:
            print(0)
    
    elif cmd[0] == 'front':
        if len(Q) == 0:
            print(-1)
        else:
            print(Q[0])

    elif cmd[0] == 'back':
        if len(Q) == 0:
            print(-1)
        else:
            print(Q[-1])