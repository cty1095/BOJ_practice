import sys
input = sys.stdin.readline
N = int(input())
weight = list(map(int,input().split()))
M = int(input())
beads = list(map(int,input().split()))

table = set([0])

for w in weight:
    new= set()
    for x in table:
        new.add(x)
        new.add(x + w)
        new.add(abs(x - w))
    table = new

result = []

for i in range(M):
    if beads[i] in table:
        result.append('Y')
    else:
        result.append('N')

print(' '.join(result))