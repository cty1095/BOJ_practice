def sudoku():
    def pre():
        board = [list(map(int, input().split())) for _ in range(9)]

        # #단일 후보 전처리 row
        # for i in range(9):
        #     if board[i].count(0) == 1:
        #         ans = 45 - sum(board[i])
        #         for j in range(9):
        #             if board[i][j] == 0:
        #                 board[i][j] = ans
        # #단일 후보 전처리 col
        # for i in range(9):
        #     sumlist = []
        #     for j in range(9):
        #         sumlist.append(board[j][i])
        #     if sumlist.count(0) == 1:
        #         ans = 45 - sum(sumlist)
        #         for j in range(9):
        #             if board[j][i] == 0:
        #                 board[j][i] = ans

        # #단일 후보 전처리 3x3 box
        # for box_row in range(3):
        #     for box_col in range(3):
        #         nums = []
        #         zero_pos = None


        #         for i in range(box_row * 3, box_row * 3 + 3):
        #             for j in range(box_col * 3, box_col * 3 + 3):
        #                 nums.append(board[i][j])
        #                 if board[i][j] == 0:
        #                     zero_pos = (i, j)
                
        #         if nums.count(0) == 1:
        #             board[zero_pos[0]][zero_pos[1]] = 45 - sum(nums)   
        return board
    
    
    def check(row,col):
        #row 검사
        checking = set()
        for i in range(9):
            checking.add(board[row][i])
        #col 검사
        for i in range(9):
            checking.add(board[i][col])
        a = row // 3
        b = col // 3
        if a ==0 and b == 0:
            for i in range(3):
                for j in range(3):
                    checking.add(board[i][j])
        elif a == 0 and b == 1:
            for i in range(3):
                for j in range(3):
                    checking.add(board[i][j+3])
        elif a == 0 and b == 2:
            for i in range(3):
                for j in range(3):
                    checking.add(board[i][j+6])
        elif a == 1 and b == 0:
            for i in range(3):
                for j in range(3):
                    checking.add(board[i+3][j])
        elif a == 1 and b == 1:
            for i in range(3):
                for j in range(3):
                    checking.add(board[i+3][j+3])
        elif a == 1 and b == 2:
            for i in range(3):
                for j in range(3):
                    checking.add(board[i+3][j+6])
        elif a == 2 and b == 0:
            for i in range(3):
                for j in range(3):
                    checking.add(board[i+6][j])
        elif a == 2 and b == 1:
            for i in range(3):
                for j in range(3):
                    checking.add(board[i+6][j+3])
        elif a == 2 and b == 2:
            for i in range(3):
                for j in range(3):
                    checking.add(board[i+6][j+6])
        candi = [1,2,3,4,5,6,7,8,9]
        list(checking)
        for sub in checking:
            if sub in candi:
                candi.remove(sub)
        return(candi)
    
    flag = False

    def dfs():
        nonlocal flag
        if flag:
            return

        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    candi = check(i,j)
                    for num in candi:
                        board[i][j] = num
                        dfs()
                        if flag == True:
                            return
                        board[i][j] = 0
                    return
        flag = True


    board = pre()
    dfs()
    return board



brd = sudoku()
# print("--------------------------------------------------")


for row in brd:
    print(*row)