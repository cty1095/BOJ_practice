import sys
from collections import deque



board = [(i,i) for i in range(101)]


N, M = map(int,input().split())

for _ in range(N+M):
    x, y = map(int,sys.stdin.readline().split())
    board[x] = (x,y)

def bfs(board):
    visited =[0] * 101
    visited[0] = 1
    visited [1] = 1
    dice = [1,2,3,4,5,6]
    q = deque()
    cnt = 0
    q.append((1,cnt))
    while q:
        elem = q.popleft()
        position = elem[0]
        cnt = elem[1]
        # move_debug.append(position)

        if position == 100:
            return cnt

        for num in dice:
            if position + num < 101:
                move = position + num
                dest = board[move][1]
                if visited[dest] == 0:
                    visited[dest] = 1
                    q.append((dest,cnt+1))
                
c=bfs(board)
print(c)

