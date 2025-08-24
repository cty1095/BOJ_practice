import sys
import heapq


N = int(sys.stdin.readline())

heap = []

for i in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            max_value = -heapq.heappop(heap)
            print(max_value)
    else:
        heapq.heappush(heap,-num)


