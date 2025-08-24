N, K = map(int,input().split())
coins = []

for i in range(N):
    coin = int(input())
    coins.append(coin)

cnt = 0
coins.reverse()

for coin in coins:
    if K >= coin:
        cnt += K // coin
        K %= coin

print(cnt)
