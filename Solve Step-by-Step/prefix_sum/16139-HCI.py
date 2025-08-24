import sys

S = sys.stdin.readline().strip()
N = len(S)
Q = int(sys.stdin.readline())

prefix = [[0] * (N+1) for _ in range(26)]

for i in range(1,N+1):
    c = S[i-1]
    for j in range(26):
        if j == ord(c) - ord('a'):
            prefix[j][i] = prefix[j][i-1] + 1
        else:
            prefix[j][i] = prefix[j][i-1]

output = []  

for _ in range(Q):
    letter, start, end = input().split()
    start = int(start)
    end = int(end)
    idx = ord(letter) - ord('a')
    ans = prefix[idx][end + 1] - prefix[idx][start]
    output.append(str(ans))

sys.stdout.write('\n'.join(output) + '\n')

# for i in range(Q):
#     letter ,start, end = input().split()
#     start = int(start)
#     end = int(end)
#     seq = ord(letter) - ord('a')
#     ans = prefix[seq][end+1] - prefix[seq][start]
#     sys.stdout.write(str(ans) + '\n')
