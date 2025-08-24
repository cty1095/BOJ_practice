import sys
input = sys.stdin.readline

N, M = map(int,input().split())
rectangle = []

for _ in range(N):
    row = input().strip()
    rectangle.append(row)

def search_square(rectangle,N,M):
    max_size = max(N,M)
    result = 0
    for i in range(N):
        for j in range(M):
            for size in range(max_size): #0,1,2
                if 0 <= (i+size) < N and 0 <= j+size < M:
                    if rectangle[i][j] == rectangle[i+size][j] == rectangle[i][j+size] == rectangle[i+size][j+size]:
                        result = max(size,result)
    return (result + 1)**2

re = search_square(rectangle,N,M)
print(re)