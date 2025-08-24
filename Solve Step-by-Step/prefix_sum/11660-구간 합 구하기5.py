import sys

N, M =map(int,sys.stdin.readline().split())

matrix = []
matrix_sum = [[0] * (N+1) for _ in range(N+1)]

for _ in range(N):
    row = list(map(int,sys.stdin.readline().split()))
    matrix.append(row)

for i in range(1,N+1):
    for j in range(1,N+1):
        matrix_sum[i][j] = matrix[i-1][j-1] + matrix_sum[i-1][j] + matrix_sum[i][j-1] -matrix_sum[i-1][j-1]
output = []
for _ in range(M):
    x1, y1, x2, y2 = map(int,sys.stdin.readline().split())
    ans = matrix_sum[x2][y2] + matrix_sum[x1-1][y1-1] - matrix_sum[x1-1][y2] - matrix_sum[x2][y1-1]    
    output.append(ans)

print('\n'.join(map(str, output)))

# print("------------")
# for row in matrix:
#     print(*row)
# print("------------")
# for row in matrix_sum:
#     print(*row)
