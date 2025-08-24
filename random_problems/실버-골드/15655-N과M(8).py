import sys
input = sys.stdin.readline

N, M = map(int,input().split())
list_N = list(map(int,input().split()))
list_N.sort()

def combination(list_N,N,M):
    result = []
    def back(start):
        if len(result) == M:
            print(*result)
            return
        
        for i in range(start,N):
            result.append(list_N[i])
            back(i)
            result.pop()
    back(0)

combination(list_N,N,M)
