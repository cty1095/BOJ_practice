import sys
input = sys.stdin.readline

M =int(input())

setA = set()

for _ in range(M):
    cmd = input().split()
    if cmd[0] == 'add':
        setA.add(int(cmd[1]))

    elif cmd[0] == 'remove':
        setA.discard(int(cmd[1])) 

    elif cmd[0] == 'check':
        if int(cmd[1]) in setA:
            print(1)
        else:
            print(0)

    elif cmd[0] == 'toggle':
        if int(cmd[1]) in setA:
            setA.remove(int(cmd[1]))
        else:
            setA.add(int(cmd[1]))

    elif cmd[0] == 'all':
        setA = {1,2,3,4,5,6,7,8,9,10,
                11,12,13,14,15,16,17,18,19,20}

    elif cmd[0] == 'empty':
        setA = set()