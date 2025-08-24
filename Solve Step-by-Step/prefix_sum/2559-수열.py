N, K = map(int,input().split())
temp = list(map(int,input().split()))


prefix = [0] * (N+1)

for i in range(1,N+1):
    prefix[i] = prefix[i-1] + temp[i-1]

max_sum = -float('Inf')
for i in range(K,N+1):
    tmp = prefix[i] - prefix[i-K]
    if tmp > max_sum:
        max_sum = tmp

print(max_sum)