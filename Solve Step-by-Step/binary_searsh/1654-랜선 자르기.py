N, K = map(int,input().split())

LAN_cables = []

for i in range(N):
    LAN = int(input())
    LAN_cables.append(LAN)

left = 1
right = max(LAN_cables)
result = 0

while left <= right:
    mid = (left +right) // 2
    cnt = 0

    for lan in LAN_cables:
        cnt += lan // mid

    if cnt < K:
        right = mid - 1
    elif cnt >= K:
        left = mid +1
        result = mid


print(result)