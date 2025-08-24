import sys
input = sys.stdin.readline

def search_mine(cube,R,C,H):
    up = [(-1,-1,-1),(-1,-1,0),(-1,-1,1),(-1,0,-1),(-1,0,0),(-1,0,1),(-1,1,-1),(-1,1,0),(-1,1,1)]
    mid = [(0,-1,-1),(0,-1,0),(0,-1,1),(0,0,-1),(0,0,1),(0,1,-1),(0,1,0),(0,1,1)]
    down = [(1,-1,-1),(1,-1,0),(1,-1,1),(1,0,-1),(1,0,0),(1,0,1),(1,1,-1),(1,1,0),(1,1,1)]
    direction = up+mid+down
    for h in range(H):
        for y in range(R):
            for x in range(C):
                if cube[h][y][x] == '.':    
                    cube[h][y][x] = 0
                if cube[h][y][x] != '*':
                    for dh,dy,dx in direction:
                        nh = h + dh
                        ny = y + dy
                        nx = x + dx
                        if 0 <= nh < H and 0<= ny < R and 0<= nx < C:
                            if cube[nh][ny][nx] == '*':
                                cube[h][y][x] += 1

    for h in range(H):
        for y in range(R):
            for x in range(C):
                if type(cube[h][y][x]) == int:
                   cube[h][y][x] = cube[h][y][x] % 10


    return cube


R,C,H = map(int,input().split())
cube = []

for _ in range(H):
    floor = []
    for _ in range(R):
        row = list(input().strip())
        floor.append(row)
    cube.append(floor)

cube1 = search_mine(cube,R,C,H)


for h in range(H):
    for y in range(R):
        print(''.join(map(str, cube1[h][y])))


