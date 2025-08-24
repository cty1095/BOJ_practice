from math import comb

N, M = map(int,input().split())

numbers = list(map(int,input().split()))


prefix = [0] * (N+1)

for i in range(1,N+1):
    prefix[i] = (prefix[i-1] + numbers[i-1]) % M #prefix % M 리스트 

count = {}
cnt = 0
for x in prefix:
    count[x] = count.get(x, 0) + 1 

for key in count:
    c=count.get(key)
    if c>= 2:
        tmp=comb(c,2)
        cnt += tmp
print(cnt)


#2차원 누적합 시간,공간복잡도 초과예상
# prefix = [[0] * (N+1) for _ in range(N+1)]
# cnt = 0
# for i in range(1,N+1):
#     for j in range(i,N+1):
#         prefix[i][j] = prefix[i][j-1] + numbers[j-1]
#         if prefix[i][j] % M == 0:
#             cnt += 1   
# print("---------------")
# for row in prefix:
#     print(*row)
#print(cnt)