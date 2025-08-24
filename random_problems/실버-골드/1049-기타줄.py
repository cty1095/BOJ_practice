import sys
input = sys.stdin.readline

N, M = map(int,input().split())
set_line = N // 6
single_line = N % 6

shop = []
for _ in range(M):
    set, single = map(int,input().split())
    shop.append([set,single])




min_set = float('inf')
single_cost = float('inf')
for i in range(M): #세트,싱글 저렴한거 찾기
    min_set = min(shop[i][0],shop[i][1] * 6,min_set)
    single_cost = min(shop[i][0],shop[i][1] * single_line, single_cost)

set_cost = set_line * min_set

total = set_cost + single_cost

print(total)
