import sys
import math
import heapq
from collections import deque
from itertools import combinations
input = sys.stdin.readline

N = int(input())  #가고싶은 채널
M = int(input())  #고장난 버튼 수


if M != 0:
    not_work_button = list(map(int,input().split()))
    work_button = ['0','1','2','3','4','5','6','7','8','9'] 

    for button in not_work_button:
        work_button.remove(str(button))

else:
    work_button = ['0','1','2','3','4','5','6','7','8','9'] 

# print(work_button)

 
def search_cnt(N):
    number = []
    str_N = str(N)
    min_cnt = abs(N-100)
    len_of_button = len(work_button)
    len_number = len(str_N)

    def backtraking(start,depth,digit):
        nonlocal min_cnt
        if depth == digit:
            tmp_number=''
            for num in number:
                tmp_number += num
            
            tmp_number = int(tmp_number)
            not_zero_number = str(tmp_number)

            if len(not_zero_number) == digit:
                cnt = abs(N - int(tmp_number))
                min_cnt = min(min_cnt,cnt+digit)
            return
        
        if start >= len_of_button:
            return
        

        #_________________________________________

        for i in range(0,len_of_button):
            number.append(work_button[i])
            backtraking(i,depth+1,digit)
            number.pop()


        

    vaild =True
    for num in str_N:
        if num not in work_button:
            vaild = False
    if vaild == True:
        min_cnt = min(len_number,min_cnt)
    else:
        backtraking(0,0,len_number)
        if len_number -1 == 0:
            pass
        else:
            backtraking(0,0,len_number-1)
        backtraking(0,0,len_number+1)

    return min_cnt



cnt = search_cnt(N)

print(cnt)