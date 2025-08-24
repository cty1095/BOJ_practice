N = int(input())
num_list = list(map(int,input().split()))
num_list.sort()
M = int(input())
is_in = list(map(int,input().split()))


for num in is_in:
    left = 0
    right = N-1
    while True:

        mid_idx = (left + right)//2
        if mid_idx < left or mid_idx > right:
            print(0)
            break
        if num_list[mid_idx] == num:
            print(1)
            break
        else:
            if num_list[mid_idx] > num:
                right = mid_idx-1
            else:
                left = mid_idx+1
