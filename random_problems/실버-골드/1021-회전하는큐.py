import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().split())
pop_list = list(map(int,input().split()))

def pop(pop_list,N):
    Q = deque([i for i in range(1,N+1)])
    cnt = 0
    for num in pop_list:
        if Q[0] == num:
            Q.popleft()
        else:
            idx = Q.index(num)
            mid_idx = len(Q)//2
            if idx <= mid_idx:
                while True:
                    if Q[0] == num:
                        Q.popleft()
                        break
                    Q.append(Q.popleft())
                    cnt += 1
            elif idx > mid_idx:
                while True:
                    if Q[0] == num:
                        Q.popleft()
                        break
                    Q.appendleft(Q.pop())
                    cnt +=1

    return cnt

cnt =pop(pop_list,N)
print(cnt)