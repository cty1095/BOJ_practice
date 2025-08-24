N = int(input())

M = [[1 , 1],[1, 0]]

p = 10**9+7

def divide(N):
    global M
    if N == 1:
        return M
    
    tmp = divide(N//2)
    result = multiple(tmp,tmp)

    if N % 2 == 0:
        return result
    
    elif N % 2 != 0:
        result = multiple(result,M)
        return result


def multiple(matrixA,martixB):
    martixC = [[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                martixC[i][j] += matrixA[i][k] * martixB[k][j]
    return selfmoduler(martixC)

def selfmoduler(matrix):
    for i in range(2):
        for j in range(2):
            matrix[i][j] %= p
    return matrix



result = divide(N)
print(result[0][1])

# result = divide(N)
# init = [[1],[0]]
# ans = [0,0]
# for i in range(2):
#     for j in range(2):
#         ans[i] += result[i][j] * init[j][0]
#         ans[i] %= p
# print(ans[0])
