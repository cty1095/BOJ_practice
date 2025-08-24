#bfs를 한번만 돌려서 먹을 물고기 찾는 로직 해야됨 


import sys
import math
import heapq
from collections import deque
from itertools import combinations
input = sys.stdin.readline


def bfs(shark_y, shark_x, baby_size):
    visited = [[False] * N for _ in range(N)]
    visited[shark_y][shark_x] = True
    Q = deque()
    Q.append((shark_y, shark_x))
    distance = 0
    direction = [(-1,0),(0,-1),(0,1),(1,0)]

    while Q:
        level_size = len(Q)
        candidates = []

        for _ in range(level_size):
            y, x = Q.popleft()

            if 0 < space[y][x] < baby_size:
                candidates.append((y, x))

            for dy, dx in direction:
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and space[ny][nx] <= baby_size:
                    visited[ny][nx] = True
                    Q.append((ny, nx))

        if candidates:
            candidates.sort()
            target_y, target_x = candidates[0]
            return distance, target_y, target_x

        distance += 1

    return -1, -1, -1

 
def babyshark(shark_y,shark_x):
    global space
    sec = 0
    baby_size = 2
    eat_cnt = 0
    while True:
        min_distance,near_y,near_x = bfs(shark_y,shark_x,baby_size)
        if min_distance == -1:
            return sec
        
        sec += min_distance
        eat_cnt += 1

        shark_y = near_y
        shark_x = near_x
        space[shark_y][shark_x] = 0
        # print(shark_y,shark_x)
        # print(sec)
        if eat_cnt == baby_size:
            baby_size += 1
            eat_cnt = 0

N = int(input())
space = []
can_eat = []
for _ in range(N):
    row = list(map(int,input().split()))
    space.append(row)

baby_y = 0
baby_x = 0
for y in range(N):
    for x in range(N):
        if space[y][x] == 9:
            baby_y = y
            baby_x = x
            break

space[baby_y][baby_x] = 0


sec = babyshark(baby_y,baby_x)
print(sec)


# 레벨단위 큐 풀이 
# import sys
# import math
# import heapq
# from collections import deque
# from itertools import combinations
# input = sys.stdin.readline


# def bfs(shark_y,shark_x,baby_size):
#     visited = [[False] * N for _ in range(N)]
#     visited[shark_y][shark_x] = True
#     distance = 0
#     Q = deque()
#     Q.append((shark_y,shark_x,distance))
#     direction = [(-1,0),(0,-1),(0,1),(1,0)]
#     result = []
#     while Q:
#         y,x,distance = Q.popleft()
#         if space[y][x] !=0 and space[y][x] < baby_size:
#             result.append((distance,y,x))
#         for dy,dx in direction:
#             ny=y+dy
#             nx=x+dx
#             if 0<= ny < N and 0<= nx < N:
#                 if space[ny][nx] <= baby_size and visited[ny][nx] == False:
#                     visited[ny][nx] = True
#                     Q.append((ny,nx,distance+1))
#     if len(result) == 0:
#         return -1
#     else:
#         result.sort()
#         return result[0]

# def babyshark(shark_y,shark_x):
#     global space
#     sec = 0
#     baby_size = 2
#     eat_cnt = 0
#     while True:
#         result = bfs(shark_y,shark_x,baby_size)
#         if result == -1:
#             return sec
        
#         min_distance,near_y,near_x=result


#         sec += min_distance
#         eat_cnt += 1
#         shark_y = near_y
#         shark_x = near_x
#         space[shark_y][shark_x] = 0
#         # print(shark_y,shark_x)
#         # print(sec)
#         if eat_cnt == baby_size:
#             baby_size += 1
#             eat_cnt = 0

# N = int(input())
# space = []
# can_eat = []
# for _ in range(N):
#     row = list(map(int,input().split()))
#     space.append(row)

# baby_y = 0
# baby_x = 0
# for y in range(N):
#     for x in range(N):
#         if space[y][x] == 9:
#             baby_y = y
#             baby_x = x
#             break

# space[baby_y][baby_x] = 0


# sec = babyshark(baby_y,baby_x)
# print(sec)

# # for row in space:
# #     print(*row)