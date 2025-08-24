# from itertools import combinations

N = int(input())

matrix = []

for i in range(N):
    row = list(map(int,input().split()))
    matrix.append(row)

# for teamA in combinations(range(N),N//2):
#     teamB = [i for i in range(N) if i not in teamA]
#     print("team A :" , teamA)
#     print("team B :" , teamB)           itertools로 조합 사용


def main(N,matrix):
    min_value = float('inf')
    selected = []
    idx = 0
    def score_cal(teamX):
        score = 0
        A = len(teamX)
        for i in range(A):
            for j in range(i+1,A):
                a = teamX[i]
                b = teamX[j]
                score += matrix[a][b] + matrix[b][a]
        return score



    def team(tmp_list,idx):

        nonlocal min_value

        if len(tmp_list) == N //2:
            teamA = tmp_list
            teamB = [i for i in range(N) if i not in teamA]
            scoreA = score_cal(teamA)
            scoreB = score_cal(teamB)
            if scoreA >= scoreB:
                value = scoreA -scoreB
            else:
                value = scoreB - scoreA
            if value < min_value:
                min_value = value
            return
        
        for i in range(idx,N): 
            tmp_list.append(i)
            team(tmp_list,i+1)
            tmp_list.pop()
            
    team(selected,idx)

    return min_value

# print("-------------------")

# for row in matrix:
#     print(*row)

# print("-----------------")
min_v=main(N,matrix)
print(min_v)