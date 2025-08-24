import sys
import math
import heapq
from collections import deque
from itertools import combinations
input = sys.stdin.readline

N = int(input())
board = [[0] * (N) for _ in range(N)]
board[0][0] = 2
K = int(input())
for _ in range(K):
    r,c = map(int,input().split())
    board[r-1][c-1] = 1

L = int(input())
turn_head = deque()

for _ in range(L):
    X, C = input().split()
    X = int(X)
    turn_head.append([X,C])

sec = 0

def dummy():
    global board
    global turn_head
    global sec
    direction = [(0,1),(1,0),(0,-1),(-1,0)] # 동 남 서 북
    dir_idx = 0
    snake = deque()
    snake.append((0,0))
    X,C = turn_head.popleft()

    while True:
        head = snake[0]
        head_y, head_x = head
        dy,dx = direction[dir_idx]
        ny = head_y + dy
        nx = head_x + dx

        if 0 <= ny < N and 0 <= nx < N and (ny,nx) not in snake:
            snake.appendleft((ny,nx))
            sec += 1
            if board[ny][nx] == 1:
                board[ny][nx] = 0

            else:
                snake.pop()
        else:
            sec += 1
            break # 뱀이 자기몸이나 벽에 만나는경우

        if sec == X:
            if C == "D":
                dir_idx = (dir_idx +1) % 4
            elif C == "L":
                dir_idx = (dir_idx +3) % 4
            
            if turn_head:
                X,C = turn_head.popleft()

dummy()
print(sec)