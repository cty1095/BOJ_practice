import sys
input = sys.stdin.readline

def gen_num(N):
    number = N
    for digit in str(N):
        number += int(digit)
    return number


max_number = 10000
self_number = [True] * (max_number+1)


for i in range(1,max_number):
    result = gen_num(i)
    if result <= max_number:
        self_number[result] = False
 

for i in range(1,max_number):
    if self_number[i] == True:
        print(i)


#visited = [False] * (max_number+1)

   # while num <= max_number:
    #     if visited[num] == False:
    #         visited[num] = True
    #         result = gen_num(num)
    #         self_number[result] = False
    #         num = result
    #     else:
    #         break