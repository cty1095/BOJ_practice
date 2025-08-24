import sys

input = sys.stdin.readline

N, C = map(int,input().split())
house = []
for i in range(N):
    h = int(input())
    house.append(h)
house.sort()


low = 0
high = house[-1] - house[0]
result = 0

while low <= high:
    mid = (low + high) // 2
    last_position = house[0]
    count = 1
    for i in range(1,N):
        if house[i] - last_position >= mid:
            count += 1
            last_position = house[i]
    if count >= C:
        result = mid
        low = mid + 1  
    else:
        high = mid - 1

print(result)
# print("result: ", result)