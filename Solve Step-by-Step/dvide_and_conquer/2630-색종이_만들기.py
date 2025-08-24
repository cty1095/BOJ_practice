N = int(input())
confetti = []

for i in range(N):
    row = list(map(int,input().split()))
    confetti.append(row)

blue_cnt = 0
white_cnt = 0

def divide(paper):
    global blue_cnt
    global white_cnt

    paper_sum = 0
    K = len(paper) #paper 길이
    for row in paper:
        paper_sum += sum(row)
    if paper_sum == K**2:
        blue_cnt += 1
    elif paper_sum == 0:
        white_cnt += 1
    else: #혼합 
        #1번 페이퍼
        paper1 = []
        for i in range(K//2):
                row = paper[i][:K//2]
                paper1.append(row)
        divide(paper1)
        
        #2번 페이퍼
        paper2 = []
        for i in range(K//2):
                row = paper[i][K//2:]
                paper2.append(row)
        divide(paper2)
        
        #3번 페이퍼
        paper3 = []
        for i in range(K//2, K):
                row = paper[i][:K//2]
                paper3.append(row)
        divide(paper3)
        
        #4번 페이퍼
        paper4 = []
        for i in range(K//2, K):
                row = paper[i][K//2:]
                paper4.append(row)
        divide(paper4)

    return blue_cnt,white_cnt

divide(confetti)

print(white_cnt)
print(blue_cnt)

