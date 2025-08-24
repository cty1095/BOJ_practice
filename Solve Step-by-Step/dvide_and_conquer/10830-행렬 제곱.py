N, B =map(int,input().split())
A = []
for i in range(N):
    row = list(map(int,input().split()))
    A.append(row)

def divide(B):
    global A
    if B == 1:
        return selfmoduler(A)
    
    tmp = divide(B//2)
    result = multiple(tmp,tmp)

    if B % 2 == 0:
        return result
    else:
        result = multiple(result,A)
        return result

    


def multiple(matrixA,matrixB):
    global N
    matrixC = [[0] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            for k in range(N):
                matrixC[i][j] += matrixA[i][k] * matrixB[k][j]
                matrixC[i][j] %= 1000
    return matrixC

def selfmoduler(matrixA):
    global N
    matrixC = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            matrixC[i][j] = matrixA[i][j] % 1000
    return matrixC


re2 = divide(B)

for row in re2:
    print(*row)