import heapq
import sys

T = int(input())


for _ in range(T):
    min_heap = []
    max_heap = []
    mid_value = []
    
    M = int(input())
    
    listM = []
    while len(listM) < M:
        listM += list(map(int, sys.stdin.readline().split()))
    
    heapq.heappush(max_heap,-listM[0])
    mid_value.append(listM[0])

    for i in range(1,M):
        if listM[i] > -max_heap[0]:
            heapq.heappush(min_heap,listM[i])
        else:
            heapq.heappush(max_heap,-listM[i])
        
        if len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

        if i % 2 == 0:
            mid_value.append(-max_heap[0])
    K = len(mid_value)
    print(K)
    for i in range(0,K,10):
        print(*mid_value[i:i+10])        
