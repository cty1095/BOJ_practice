import sys
import math
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    a = x2 -x1
    b = y2 - y1
    d = math.sqrt(a**2 + b**2)

    if r1 == r2 and d == 0: #두원이 같은 원(합동)
        print(-1)
    elif d > r1 + r2: #두 원 떨어짐
        print(0)
    elif d < abs(r1-r2): #한원 안에 다른원있는데 안만남
        print(0)
    elif d == r1 +r2 : #외접 
        print(1)
    elif d == abs(r1-r2): #내접
        print(1)
    else:
        print(2)