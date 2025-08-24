N = int(input())
confetti = []

for i in range(N):
    row = input()
    confetti.append(row)



def conquer(a,b,c,d):
        s = "(" + str(a) + str(b) + str(c) + str(d) + ")"
        return s

def divide(paper):

    paper_sum = 0
    K = len(paper) #paper 길이
    for i in range(K):
        for j in range(K):
              paper_sum += int(paper[i][j])
    
    if paper_sum == K**2: #모두 1
        return 1
    elif paper_sum == 0:  #모두 0
        return 0
    else: 
        #괄호 생성
        #1번 페이퍼
        paper1 = []
        for i in range(K//2):
                row = paper[i][:K//2]
                paper1.append(row)
        a=divide(paper1)
        
        #2번 페이퍼
        paper2 = []
        for i in range(K//2):
                row = paper[i][K//2:]
                paper2.append(row)
        b=divide(paper2)
        
        #3번 페이퍼
        paper3 = []
        for i in range(K//2, K):
                row = paper[i][:K//2]
                paper3.append(row)
        c =divide(paper3)
        
        #4번 페이퍼
        paper4 = []
        for i in range(K//2, K):
                row = paper[i][K//2:]
                paper4.append(row)
        d = divide(paper4)

        s = conquer(a,b,c,d)


              

    return s

ans = divide(confetti)
print(ans)