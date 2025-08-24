import sys
import math
import heapq
from collections import deque
from itertools import combinations

input = sys.stdin.readline

N, M = map(int,input().split())
parent = [i for i in range(N+1)]

def find(a):
    global parent
    if parent[a] == a:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a,b):
    global parent
    root_a = find(a)
    root_b = find(b)
    if root_a == root_b:
        return

    else:
        parent[root_a] = root_b
        return


for _ in range(M):
    cmd, a, b = map(int,input().split())
    if cmd == 0:
        union(a,b)
    if cmd == 1:
        root_a = find(a)
        root_b = find(b)
        if root_a == root_b:
            print("YES")
        else:
            print("NO")
# print(parent)