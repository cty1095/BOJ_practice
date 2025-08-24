N, M = map(int,input().split())

board = []

for i in range(N):
    row = input()
    board.append(row)

INF = 9999999999
minvalue = INF

def check(chess):
    cnt_w = 0  #start white
    cnt_b = 0  #start black

    for i in range(8):
        for j in range(8):
            if (i+j)%2 == 0:
                expected_w = 'W'
                expected_b = 'B'
            else:
                expected_w = "B"
                expected_b = "W"

            if chess[i][j] != expected_w:
                cnt_w += 1
            if chess[i][j] != expected_b:
                cnt_b += 1

    return min(cnt_w, cnt_b)


for i in range(N-7):
    for j in range(M-7):
        tmp_chess = []
        for k in range(i,i+8):
            row = board[k][j:j+8]
            tmp_chess.append(row)
        value = check(tmp_chess)
        if minvalue > value:
            minvalue= value

print(minvalue) 

