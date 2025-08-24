import sys
import math
input = sys.stdin.readline

N = int(input())
human = []
rank = [0] * N
for _ in range(N):
    weight , height = map(int,input().split())
    human.append([weight,height])


for i in range(N):
    count = 0
    for j in range(N):
        if i != j and human[j][0] > human[i][0] and human[j][1] > human[i][1]:
            count += 1
    rank[i] = count + 1
print(*rank)