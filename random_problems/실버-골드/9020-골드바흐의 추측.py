import sys
import math
from collections import deque
input = sys.stdin.readline

def gold(N):
    global prime
    start = N //2
    end = N//2
    while True:
        if prime[start] ==True and prime[end] ==True:
            return start, end
        else:
            start -= 1
            end += 1

                
    


def sieve_of_eratosthenes(max_number):
    prime = [True] * (max_number+1)
    prime[0] = False
    prime[1] = False
    max_range=int(math.sqrt(max_number)) + 1
    prime_list =[]
    for i in range(2,max_range):
        if prime[i] == True:
            for multiple in range(i * 2, max_number + 1, i):
                prime[multiple] = False
    
    for i in range(2,max_number+1):
        if prime[i] == True:
            prime_list.append(i)
    
    return prime_list,prime


T = int(input())
max_number = 10000
prime_list,prime = sieve_of_eratosthenes(max_number)


for _ in range(T):
    N = int(input())
    answer1,answer2 = gold(N)
    print(answer1,answer2)