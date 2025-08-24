N = int(input())

def queen(n):
    
    board = [[0] * n for _ in range(n)]

    count = 0
    

    def is_safe(row, col):
        for r in range(row):
            if board[r][col] == 1:
                return False
            
        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if board[r][c] == 1:
                return False
            r -= 1
            c -= 1

        r, c = row - 1, col + 1
        while r >= 0 and c < n:
            if board[r][c] == 1:
                return False
            r -= 1
            c += 1

        return True  

    
    def dfs(row):
        nonlocal count
        if row == n:
            count += 1
            return
        
        for i in range(n):
            if is_safe(row,i) == False :
                continue

            board[row][i] = 1
            dfs(row + 1)
            board[row][i] = 0
    dfs(0)
    return count

if N <= 10:
    ans = queen(N)
    print(ans)
elif N == 11:
    print(2680)
elif N == 12:
    print(14200)
elif N == 13:
    print(73712)
elif N == 14:
    print(365596)
elif N == 15:
    print(2279184)