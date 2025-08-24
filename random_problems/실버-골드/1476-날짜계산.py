import sys
input = sys.stdin.readline

E, S, M = map(int,input().split())


def gen_date(E,S,M):
    max_Earth = 16
    max_Sun = 29
    max_Moon = 20
    Earth = 1
    Sun = 1
    Moon = 1
    year = 1
    while True:
        if Earth == E and Sun == S and Moon ==M :
            return year
        year += 1
        Earth += 1 
        Sun += 1
        Moon += 1
        if Earth == max_Earth:
            Earth -= 15
        if Sun == max_Sun:
            Sun -=28
        if Moon == max_Moon:
            Moon -= 19

year = gen_date(E,S,M)
print(year)