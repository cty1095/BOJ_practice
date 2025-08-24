import sys
input = sys.stdin.readline

N, M = map(int,input().split())
list_N = list(map(int,input().split()))
list_N.sort()

def combination(list_N,M):
    visited = [False] * len(list_N)
    result = []
    def back(start):
        if len(result) == M:
            print(*result)
            return
        
        for i in range(start,len(list_N)):
            result.append(list_N[i])
            back(i+1)
            result.pop()
            visited[i] = False
    back(0)

combination(list_N,M)
