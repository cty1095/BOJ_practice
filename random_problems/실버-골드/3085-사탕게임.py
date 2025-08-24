import sys
input = sys.stdin.readline

N = int(input())
bomboni = []
for _ in range(N):
    row = list(input().strip())
    bomboni.append(row)

def Search_LongCandy(bomboni,N):
    def swap_row(max_candy):
        for y in range(N):
            tmp = "X"
            for x in range(N-1):
                tmp = bomboni[y][x]
                bomboni[y][x] = bomboni[y][x+1]
                bomboni[y][x+1] = tmp
                max_candy=max(get_max_candy(max_candy),max_candy)
                tmp = bomboni[y][x]
                bomboni[y][x] = bomboni[y][x+1]
                bomboni[y][x+1] = tmp
        return max_candy
    def swap_col(max_candy):
        for x in range(N):
            tmp = "X"
            for y in range(N-1):
                tmp = bomboni[y][x]
                bomboni[y][x] = bomboni[y+1][x]
                bomboni[y+1][x] = tmp
                max_candy=max(get_max_candy(max_candy),max_candy)
                tmp = bomboni[y][x]
                bomboni[y][x] = bomboni[y+1][x]
                bomboni[y+1][x] = tmp

        return max_candy
    def get_max_candy(max_candy):
        #row 검사
        for i in range(N):
            candy = 1
            for j in range(N-1):
                if bomboni[i][j] == bomboni[i][j+1]:
                    candy += 1
                    max_candy = max(max_candy,candy)            
                else:
                    candy = 1
        #col 검사
        for i in range(N):
            candy = 1
            for j in range(N-1):
                if bomboni[j][i] ==bomboni[j+1][i]:
                    candy += 1
                    max_candy = max(max_candy,candy)
                else:
                    candy = 1

        return max_candy
    max_candy = get_max_candy(1)
    max_candy = swap_row(max_candy)
    max_candy = swap_col(max_candy)
    return max_candy

result = Search_LongCandy(bomboni,N)
print(result)



    