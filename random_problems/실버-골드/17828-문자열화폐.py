N, X = map(int, input().split())

if X > 26 * N:
    print('!')
    exit() 

remain = X - N
word = [1] * N
idx = N - 1

while remain > 0 and idx >= 0:
    add = min(25, remain)
    word[idx] += add
    remain -= add
    idx -= 1

for val in word:
    print(chr(ord('A') + val - 1), end='')
