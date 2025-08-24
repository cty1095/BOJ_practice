N = int(input())
wating = list(map(int,input().split()))
wating.sort()


prefix = [0] * (N+1)

for i in range(1,N+1):
    prefix[i] = prefix[i-1] + wating[i-1]

print(sum(prefix))