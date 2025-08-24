import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A, B = map(int,input().split())
M = int(input())

tree = [[] for _ in range(N+1)]
for _ in range(M):
    parent, child = map(int,input().split()) 
    tree[parent].append(child)
    tree[child].append(parent)

def bfs(tree,A,B):
    q = deque()
    q.append([A,0])
    visited = [False] * (N+1)
    
    while q:
        person, count = q.popleft()
        if person == B:
            return count
        if visited[person] == False:
            for next_person in tree[person]:
                q.append([next_person,count+1])
                visited[person] = True

chon = bfs(tree,A,B)
if chon == None:
    print(-1)
else:
    print(chon)          





# for row in tree:
#     print(*row)
