import sys
import heapq


N = int(sys.stdin.readline())

heap = []
matrix = []


for i in range(N):
    row = list(map(int,sys.stdin.readline().split()))
    matrix.append(row)
    if i == (N-1):
        for j in range(N):
            heapq.heappush(heap,(-row[j],i,j))

for _ in range(N):
    max_value,i,j = heapq.heappop(heap)
    max_value = -max_value
    if i > 0:
        heapq.heappush(heap,(-matrix[i-1][j],i-1,j))


print(max_value)
# print(heap)
# max_value,idx_i,idx_j = heapq.heappop(heap)
# max_value = -max_value
# print(max_value)