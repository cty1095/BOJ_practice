import sys
input = sys.stdin.readline

N, playerA, playerB = map(int,input().split())
round = 0
while playerA != playerB:
    playerA = (playerA + 1) // 2
    playerB = (playerB + 1) // 2
    round += 1

print(round)