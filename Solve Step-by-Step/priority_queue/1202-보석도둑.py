import heapq
import sys


N,K = map(int,sys.stdin.readline().split())
zems = []
bags = []
max_heap=[]

for _ in range(N):
    zem = list(map(int,sys.stdin.readline().split()))
    zems.append(zem)

for _ in range(K):
    bag_m = int(sys.stdin.readline())
    bags.append(bag_m)

zems.sort()
bags.sort()

value_sum = 0
j = 0  

for bag in bags:
    
    while j < N and zems[j][0] <= bag:
        heapq.heappush(max_heap, -zems[j][1]) 
        j += 1
    
    if max_heap:
        value_sum += -heapq.heappop(max_heap)

print(value_sum)