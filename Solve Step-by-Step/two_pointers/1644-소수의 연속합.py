import math

def prime_sieve(n):
    prime = [True] * (N+1)
    prime[0] = False
    prime[1] = False
    prime_list = []

    for i in range(2, int(math.sqrt(N))+1): 
        if prime[i] == True:    
        
            for j in range(i*i,N+1,i):
                prime[j] = False


    for i in range(2,N+1):
        if prime[i] == True:
            prime_list.append(i)

    return prime_list

def prefix_prime(prime_list):
    n = len(prime_list)
    prefix = [0] * (n+1)

    for i in range(1,n+1):
        prefix[i] = prefix[i-1] + prime_list[i-1]
    
    return prefix
    
def two_pointer(prefix,N):
    max_idx = len(prefix)
    left = 0
    right = 0
    cnt = 0

    while right <= max_idx-1:
        if prefix[right] - prefix[left] == N:
            cnt += 1
            left += 1
        elif prefix[right] - prefix[left] < N:
            right += 1
        elif prefix[right] - prefix[left] > N:
            left += 1
    return cnt


N = int(input())

prime_lst = prime_sieve(N)
# print(prime_lst)
prefix = prefix_prime(prime_lst)
# print(prefix)
result = two_pointer(prefix,N)
print(result)