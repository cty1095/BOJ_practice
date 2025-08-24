N = int(input())
D = []
for i in range(N):
    a, b = map(int,input().split())
    D.append(a)
    if i == N-1:
        D.append(b)

def minmult(d,n):
    M = [([-1] * (n+1)) for _ in range(n+1)]
    for i in range(1,n+1):
        M[i][i] = 0
    
    for diagonal in range(1,n):
        for i in range(1,n-diagonal+1):
            j = i + diagonal
            M[i][j] = minimum(M,d,i,j)
    return M


def minimum(M,d,i,j):
    INF = int(1e9)
    minValue = INF

    for k in range(i,j):
        value = M[i][k] + M[k+1][j]
        value += d[i-1] * d[k] * d[j]
        if minValue > value :
            minValue = value
    return minValue

M = minmult(D,N)

print(M[1][N])