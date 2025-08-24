#알파벳 사용 관리를 집합으로말고 false * 26개의 리스트로 인덱스로 관리...하면 더빠를듯


import sys
import math
from collections import deque
from itertools import combinations
sys.setrecursionlimit(10**6) 
input = sys.stdin.readline




R,C = map(int,input().split())

used_abc = [False] * 26

matrix = []
for _ in range(R):
    row = input().strip()
    matrix.append(row)

direction = [(-1,0),(1,0),(0,-1),(0,1)]

def dfs(y, x, used):
    global max_cnt
    max_cnt = max(max_cnt, len(used)) 

    for dy, dx in direction:
        ny, nx = y + dy, x + dx
        if 0 <= ny < R and 0 <= nx < C and matrix[ny][nx] not in used:
            used.add(matrix[ny][nx])
            dfs(ny, nx, used)
            used.remove(matrix[ny][nx])

max_cnt = 0
dfs(0, 0, {matrix[0][0]}) 
print(max_cnt)