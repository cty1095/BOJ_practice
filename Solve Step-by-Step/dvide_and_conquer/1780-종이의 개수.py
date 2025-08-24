import sys

N = int(input())
confetti = []

for i in range(N):
    row = list(map(int,sys.stdin.readline().split()))
    confetti.append(row)



minus_cnt = 0
zero_cnt = 0
plus_cnt = 0

def divide(paper):
    global minus_cnt
    global zero_cnt
    global plus_cnt

    paper_minus = 0
    paper_zero = 0
    paper_plus = 0
    K = len(paper) #paper 길이
    
    for row in paper:
        paper_minus += row.count(-1)
        paper_zero += row.count(0)
        paper_plus += row.count(1)

    if paper_minus == K**2:
        minus_cnt += 1
    elif paper_zero == K**2:
        zero_cnt += 1
    elif paper_plus == K**2:
        plus_cnt += 1
    else: #혼합 
        A = (K//3)
        #1번 페이퍼
        paper1 = []
        for i in range(A):
                row = paper[i][:A]
                paper1.append(row)
        divide(paper1)
        
        #2번 페이퍼
        paper2 = []
        for i in range(A):
                row = paper[i][A:A*2]
                paper2.append(row)
        divide(paper2)
        
        #3번 페이퍼
        paper3 = []
        for i in range(A):
                row = paper[i][A*2:]
                paper3.append(row)
        divide(paper3)
        
        #4번 페이퍼
        paper4 = []
        for i in range(A,A*2):
                row = paper[i][:A]
                paper4.append(row)
        divide(paper4)
        
        #5번 페이퍼
        paper5 = []
        for i in range(A,A*2):
                row = paper[i][A:A*2]
                paper5.append(row)
        divide(paper5)
        
        #6번 페이퍼
        paper6 = []
        for i in range(A,A*2):
                row = paper[i][A*2:]
                paper6.append(row)
        divide(paper6)
        

        #7번 페이퍼
        paper7 = []
        for i in range(A*2,K):
                row = paper[i][:A]
                paper7.append(row)
        divide(paper7)
        
        #8번 페이퍼
        paper8 = []
        for i in range(A*2,K):
                row = paper[i][A:A*2]
                paper8.append(row)
        divide(paper8)
        
        #9번 페이퍼
        paper9 = []
        for i in range(A*2,K):
                row = paper[i][A*2:]
                paper9.append(row)
        divide(paper9)
        

    return minus_cnt, zero_cnt, plus_cnt

divide(confetti)

print(minus_cnt)
print(zero_cnt)
print(plus_cnt)

