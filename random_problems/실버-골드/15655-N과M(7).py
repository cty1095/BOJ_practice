import sys
input = sys.stdin.readline

N, M = map(int,input().split())
list_N = list(map(int,input().split()))
list_N.sort()

def repeated_per(list_N,N,M):
    result = []
    def back():
        if len(result) == M:
            print(*result)
            return
        for i in range(N):
            result.append(list_N[i])
            back()
            result.pop()
repeated_per(list_N,N,M)