import sys
import math
from collections import deque
from itertools import combinations
input = sys.stdin.readline

N, M = map(int,input().split())
room= []
start_y,start_x,start_direction = map(int,input().split())

for _ in range(N):
    row = list(map(int,input().split()))
    room.append(row)

def clean_room(start_y,start_x,start_direction):
    cleand = [[False] * M for _ in range(N)]
    move = [(-1,0),(0,1),(1,0),(0,-1)] # 북 동 남 서 순
    cnt =0
    Q = deque()
    Q.append([start_y,start_x,start_direction])
    while Q:
        now_y,now_x,now_direction = Q.popleft()
        if room[now_y][now_x] == 0 and cleand[now_y][now_x] ==False:
            cleand[now_y][now_x] = True
            cnt += 1
        
        around_wall = True


        for dy,dx in move: #주위 벽검사
            ny = now_y + dy
            nx = now_x + dx
            if 0 <= ny < N and 0 <= nx < M :
                if room[ny][nx] == 0 and cleand[ny][nx] == False:
                    around_wall = False
        
        if around_wall == True:
            cross_direction = (now_direction + 2) % 4
            my,mx = move[cross_direction]
            dy = now_y+my
            dx = now_x +mx
            if room[dy][dx] == 0:
                Q.append([dy,dx,now_direction])
            else:
                return cnt
        else:
            left_loataion_direction = (now_direction+3)%4
            my,mx = move[left_loataion_direction]
            dy = now_y+my
            dx = now_x +mx
            if room[dy][dx] == 0 and cleand[dy][dx] == False:
                Q.append([dy,dx,left_loataion_direction])
            else:
                Q.append([now_y,now_x,left_loataion_direction])
    
    
    return cnt          

cnt = clean_room(start_y,start_x,start_direction)
print(cnt)