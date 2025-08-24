N, M =map(int,input().split())
matrixA = []
for i in range(N):
    row = list(map(int,input().split()))
    matrixA.append(row)

M, K = map(int,input().split())
matrixB = []
for i in range(M):
    row = list(map(int,input().split()))
    matrixB.append(row)

matrixC = [[0] * K for _ in range(N)]

for i in range(N):
    for j in range(K):
        for k in range(M):
            matrixC[i][j] += matrixA[i][k] * matrixB[k][j]

for row in matrixC:
    print(*row)