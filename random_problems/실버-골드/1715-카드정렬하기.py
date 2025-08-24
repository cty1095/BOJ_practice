import sys
import math
import heapq
from collections import deque
from itertools import combinations
input = sys.stdin.readline


heap = []
N = int(input())
for _ in range(N):
    cards = int(input())
    heapq.heappush(heap,cards)


sum_total = 0
while len(heap) > 1:
    card1 = heapq.heappop(heap)
    card2 = heapq.heappop(heap)
    sum_card = card1+card2
    sum_total += sum_card
    heapq.heappush(heap,sum_card)

print(sum_total)