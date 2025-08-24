N, K = map(int,input().split())
p = 10**9 + 7

# {(n! % p) * (k!**(p-2) % p) * ((n-k)!**(p-2) % p )} % p

maximum = 4000000
factorial = [1] * (maximum+1)

for i in range(2,maximum):   # n! % p
    factorial[i] = (factorial[i-1] * i) % p

ans = (factorial[N] * pow(factorial[K],p-2,p) * pow(factorial[N-K],p-2,p)) % p

print(ans)