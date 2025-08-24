import sys
import heapq

N = int(input())
heap = []

for _ in range(N):
    row = list(map(int,sys.stdin.readline().split()))
    for num in row:
        if len(heap) < N:
            heapq.heappush(heap,num)
        else:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap,num)
print(heap[0])

