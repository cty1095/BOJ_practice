import sys
import math
from collections import deque
from itertools import combinations
input = sys.stdin.readline

def floyd(graph,N):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1

    return graph
            

N = int(input())
graph = []
for _ in range(N):
    row = list(map(int,input().split()))
    graph.append(row)

dp = floyd(graph,N)
for row in dp:
    print(*row)

