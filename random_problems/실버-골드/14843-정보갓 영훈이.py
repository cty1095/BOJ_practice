#소수2자리 까지만 출력
#포멧팅


import sys
input = sys.stdin.readline

N = int(input())
scores = []
score = 0
for i in range(N):
    S, A, T, M = map(float,input().split())
    A = int(A)
    T = int(T)
    M = int(M)
    score +=  (S * (1+(1/A)) * (1+(M/T))) / 4

scores.append(score)

P = int(input())
for i in range(P):
    R = float(input())
    scores.append(R)

scores.sort(reverse=True)
rank = scores.index(score) + 1
younghoon_per=(rank/(P+1)) * 100


if younghoon_per <= 15:
    print('The total score of Younghoon "The God" is {sco:.2f}.'.format(sco=score))
else:
    print('The total score of Younghoon is {sco:.2f}.'.format(sco=score))