import sys
input = sys.stdin.readline

N, M = map(int,input().split())
list_N = list(map(int,input().split()))
list_N.sort()

def combination(list_N,N,M):
    result = []
    mem = set([])
    def back(start):
        if len(result) == M:
            t = tuple(result)
            if t in mem:
                return
            else:
                mem.add(t)
                print(*t)
                return
        
        for i in range(start,N):
            result.append(list_N[i])
            back(i+1)
            result.pop()
 
    back(0)

combination(list_N,N,M)
