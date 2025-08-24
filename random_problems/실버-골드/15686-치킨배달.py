import sys
import math
from collections import deque
from itertools import combinations
input = sys.stdin.readline

def find_chicken_distance(city,max_chickens):
    shop_chicken =[]
    home = []
    tmp = []
    min_chicken_distance = float('inf') 
    for y in range(N):
            for x in range(N):
                if city[y][x] == 2:
                    shop_chicken.append((y,x))
                elif city[y][x] == 1:
                    home.append((y,x))

    def backtracking(start,cnt):
        nonlocal min_chicken_distance
        if cnt == max_chickens:
            chicken_distance = 0
            
            for hy,hx in home:
                min_distance = float('inf')
                for cy,cx in tmp:
                    distance = abs(hy-cy) + abs(hx-cx)
                    min_distance = min(min_distance,distance)
                chicken_distance += min_distance
        
            min_chicken_distance = min(chicken_distance,min_chicken_distance)
            return
        
        for i in range(start,len(shop_chicken)):
            y,x = shop_chicken[i]
            tmp.append((y,x))
            backtracking(i+1,cnt+1)
            tmp.pop()


    backtracking(0,0)
    return min_chicken_distance, home, shop_chicken
#-------------------------------------

N,max_chickens = map(int,input().split())

city = []
for _ in range(N):
    row = list(map(int,input().split()))
    city.append(row)

distance, home,shop = find_chicken_distance(city,max_chickens)
print(distance)
# print(home)
# print(shop)