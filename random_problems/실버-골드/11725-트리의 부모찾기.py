import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    A, B = map(int,input().split())
    tree[A].append(B)
    tree[B].append(A)

def bfs(tree):
    result = [[] for _ in range(N+1)]
    visited = [False] * (N+1)
    root = 1
    Q = deque()
    Q.append(root)

    while Q:
        node = Q.popleft()
        if visited[node] == False:
            for next in tree[node]: #next = 4,6
                if visited[next] == False:
                    result[next].append(node)
                visited[node] = True
                Q.append(next)

    return result

result = bfs(tree)
for i in range(2,N+1):
    print(*result[i])

