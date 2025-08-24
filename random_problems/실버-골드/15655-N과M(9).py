import sys
input = sys.stdin.readline

N, M = map(int,input().split())
list_N = list(map(int,input().split()))
list_N.sort()

def combination(list_N,N,M):
    result = []
    visited = [False] * N
    mem = set([])
    def back():
        if len(result) == M:
            t = tuple(result)
            if t in mem:
                return
            else:
                mem.add(t)
                print(*t)
                return
        
        for i in range(N):
            if visited[i] == False:
                visited[i] = True
                result.append(list_N[i])
                back()
                result.pop()
                visited[i] = False
    back()

combination(list_N,N,M)
