import sys
input = sys.stdin.readline

def flower(flower_cnt,total_cost):
    direction = [(-1,0),(1,0),(0,-1),(0,1),(0,0)] #상하좌우가운데
    global visited
    global field
    global answer


    def search_flower(y,x):        
        for dy,dx in direction:
            ny = y + dy
            nx = x + dx
            if visited[ny][nx]:
                return False
        return True


    def plant_seed(y,x):
        tmp_cost = 0
        for dy,dx in direction:
            ny = y + dy
            nx = x + dx
            tmp_cost += field[ny][nx]
            visited[ny][nx] = True         
        return tmp_cost


    def remove_flower(y,x):
        for dy,dx in direction:
            ny = y + dy
            nx = x + dx
            visited[ny][nx] = False

    if flower_cnt == 3:
        answer = min(answer, total_cost)
        return

    for y in range(1, N-1):
        for x in range(1, N-1):
            if search_flower(y, x) == True:
                cost = plant_seed(y, x)
                flower(flower_cnt + 1, total_cost + cost)
                remove_flower(y, x)

N = int(input())
field = []
visited = [[False] * N for _ in range(N)]
for _ in range(N):
    row = list(map(int,input().split()))
    field.append(row)


answer = float('inf')
flower(0,0)
print(answer)
# for row in visited:
#     print(*row)
