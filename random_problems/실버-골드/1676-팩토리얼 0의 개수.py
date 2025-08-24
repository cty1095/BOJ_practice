# math.factorial 쓰는방법
# import sys
# import math
# from collections import deque

# input = sys.stdin.readline

# N = int(input())
# factorial = str(math.factorial(N))
# A=len(factorial)

# cnt = 0
# for i in range(1,A+1):
#     if factorial[-i] == "0":
#         cnt += 1
#     else:
#         break
# print(cnt)


# 5가 몇번곱해졌는지 카운팅
import sys

input = sys.stdin.readline

N = int(input())
cnt =0
for i in range(1,N+1):
    if i % 5 == 0:
        cnt += (i // 5)
print(cnt)