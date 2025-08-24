import sys
sys.setrecursionlimit(10**7)


def squared(histogram,left_idx,right_idx):


    if left_idx == right_idx:  #막대가 한개
        return histogram[right_idx]
    elif right_idx - left_idx == 1: #막대가 두개
        if histogram[left_idx] < histogram[right_idx]:
            return max(2 * histogram[left_idx] , histogram[right_idx])
        else:
            return max(2 * histogram[right_idx],histogram[left_idx])

    
    #막대가 최소 3개
    mid_idx = (left_idx+right_idx)//2

    low = high = mid_idx
    height = histogram[mid_idx]
    max_mid = height

    while left_idx < low or high < right_idx:
        if high < right_idx and (low == left_idx or histogram[low - 1] < histogram[high + 1]):
            high += 1
            height = min(height, histogram[high])
        else:
            low -= 1
            height = min(height, histogram[low])
        max_mid = max(max_mid, height * (high - low + 1))


    left_squared = squared(histogram,left_idx,mid_idx)
    right_squared = squared(histogram,mid_idx+1,right_idx)

    return max(max_mid,left_squared,right_squared)

output = []
while True:
    input_list = list(map(int,sys.stdin.readline().split()))
    N = input_list[0]
    if N == 0:
        break
    histo = input_list[1:]
    ans = squared(histo,0,N-1)
    output.append(ans)
print('\n'.join(map(str, output)))



