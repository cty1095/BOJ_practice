# 코드 구현은 했는데 치명적인 오류
# 현재 구현한 코드는 색갈 차이의합을 구함
# B B        B W
# W W   와   W B 는 색갈 차이의 합이 같음 (정답 아님)
#1번의 경우 1 + 1 -1 -1 = 0
#2번의 경우 1 -1 +1 -1 = 0
# 다시 구현하자 코드...



N, M, K = map(int,input().split())
chess = []
for i in range(N):
    row = input()
    chess.append(row)

chess_01 = [[0] * (M) for _ in range(N)]
chess_sum = [[0] * (M+1) for _ in range(N+1)]
# chess_white = [[0] * (M+1) for _ in range(N+1)]

#체스판 B = 1 , W = -1 int로 재배열
for i in range(N):
    for j in range(M):
        if chess[i][j] == 'B':
            chess_01[i][j] = 1 #b = 1
        elif chess[i][j] == 'W':
            chess_01[i][j] = -1 #w = -1
#체스판 누적합
for i in range(1,N+1):
    for j in range(1,M+1):
        chess_sum[i][j] = chess_sum[i-1][j] + chess_sum[i][j-1] + chess_01[i-1][j-1] - chess_sum[i-1][j-1]

#K * K 의 체스판 
K_black = [[0] * K for _ in range(K)] #B =1 , W = -1
K_white = [[0] * K for _ in range(K)] #W = 1 ,B = -1

for i in range(K):
    for j in range(K):
        if (i + j) % 2 == 0:
            K_black[i][j] = 1
            K_white[i][j] = -1
        else:
            K_black[i][j] = -1
            K_white[i][j] = 1

#K_black(맨왼쪽모서리 블랙인경우) 누적합
K_black_sum = [[0] * (K+1) for _ in range(K+1)]
for i in range(1,K+1):
    for j in range(1,K+1):
            K_black_sum[i][j] = K_black_sum[i-1][j] + K_black_sum[i][j-1] + K_black[i-1][j-1] - K_black_sum[i-1][j-1]

#K_white(맨왼쪽모서리 화이트인경우) 누적합
K_white_sum = [[0] * (K+1) for _ in range(K+1)]
for i in range(1,K+1):
    for j in range(1,K+1):
            K_white_sum[i][j] = K_white_sum[i-1][j] + K_white_sum[i][j-1] + K_white[i-1][j-1] - K_white_sum[i-1][j-1]


min_value =999999999
for i in range(1, N-K+2):
    for j in range(1, M-K+2):

        tmp = chess_sum[i+K-1][j+K-1] - chess_sum[i-1][j+K-1] - chess_sum[i+K-1][j-1]+ chess_sum[i-1][j-1]
        error_black = abs(tmp - K_black_sum[K][K]) // 2
        error_white = abs(tmp - K_white_sum[K][K]) // 2
        min_value = min(min_value, error_black, error_white)
        
print(min_value)



# print("------------")
# print(min_value)
# print("-----")
# for row in chess_01:
#     print(*row)
# print("-----")
# for row in chess_sum:
#     print(*row)
# print("-----")
# for row in K_black_sum:
#     print(*row)
