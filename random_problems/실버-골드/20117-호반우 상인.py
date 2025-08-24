N = int(input())


hobanwo = list(map(int,input().split()))
hobanwo.sort()
result = 0

if N % 2 == 0: #짝
    mid_idx = (N//2) 
    num = N//2
    idx = N-1
    for i in range(num):
        result += hobanwo[idx] * 2
        idx -= 1
    print(result)
else:
    mid_idx = (N+1)//2 -1
    num = N // 2
    idx = N-1
    for i in range(num):
        result += hobanwo[idx] * 2
        idx -= 1
    result += hobanwo[mid_idx]
    print(result)



