N = int(input())   # =3
K = int(input())   # =7

low = 1
high = K
result = 0

while low <= high:
    mid = (low + high) // 2 
    cnt = 0

    for i in range(1,N+1): 
        cnt += min(mid//i,N)

    if cnt < K:
        low = mid + 1
    elif cnt >= K:
        high = mid - 1
        result = mid

print(result)