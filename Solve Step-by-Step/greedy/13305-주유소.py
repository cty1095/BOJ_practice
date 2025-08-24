N = int(input())
distance = list(map(int,input().split()))
city = list(map(int,input().split()))


cost = distance[0] * city[0]
min_cost = city[0]

for i in range(1,N-1):
    if city[i] < min_cost:
        tmp = city[i] * distance [i]
        cost += tmp
        min_cost = city[i]
    else:
        tmp = min_cost * distance[i]
        cost += tmp

print(cost)