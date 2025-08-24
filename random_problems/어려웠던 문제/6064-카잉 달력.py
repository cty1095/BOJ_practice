import sys
import math
input = sys.stdin.readline


def gen_date(M,N,x,y):
    #year≡x(modM)
    #year≡y(modN)
    #중국인의 나머지 정리
    #year % M == x 가 성립하려면 year의 범위는 x,x+M,x+2M,...
    #year의 범위에서 year % N ==y 가 성립하는지만 확인
    year = x
    g = math.gcd(M, N)
    lcm = (M*N)//g
    while year <= lcm:
        if (year - 1) % N + 1 == y:
            return year
        else:
            year += M
    
    return -1

T = int(input())
for _ in range(T):
    M, N, x, y = map(int,input().split())
    year = gen_date(M,N,x,y)
    print(year)


# 이렇게 푸니깐 시간초과 -->중국인의 나머지 정리 이용
# def gen_date(M,N,x,y):
#     max_X = M+1
#     max_Y = N+1
#     one = 1
#     two = 1
#     year = 1
#     while True:
#         if one == x and two == y:
#             return year
#         if one == M and two == N:
#             return 'last year'
#         year += 1
#         one += 1 
#         two += 1
#         if one == max_X:
#             one -= M
#         if two == max_Y:
#             two -=N