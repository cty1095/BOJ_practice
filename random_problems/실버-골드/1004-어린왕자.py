import sys 
import math
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    x1, y1, x2, y2 = map(int,input().split())
    N = int(input())
    cnt = 0
    for i in range(N):
        cx, cy, cr = map(int,input().split())
        start_d = math.sqrt((x1-cx)**2 + (y1-cy)**2)
        end_d = math.sqrt((x2-cx)**2 + (y2-cy)**2)
        if (start_d < cr and end_d > cr) or (start_d > cr and end_d <cr):
            cnt += 1
    print(cnt)
        