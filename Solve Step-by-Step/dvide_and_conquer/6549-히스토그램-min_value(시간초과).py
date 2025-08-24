import sys
sys.setrecursionlimit(10**7)


def squared(histogram,left_idx,right_idx):

    if left_idx > right_idx:
        return 0
    
    # min_value = min(histogram)
    # min_idx = histogram.index(min_value) 
    # 2번 순회 => 1번 순회로 최적화
    min_value = histogram[left_idx]
    min_idx = left_idx

    for i in range(left_idx, right_idx+1):
        if histogram[i] < min_value:
            min_value = histogram[i]
            min_idx = i


    width = right_idx - left_idx + 1
    min_squared = width * min_value

    left_squared = squared(histogram,left_idx,min_idx-1)
    right_squared = squared(histogram,min_idx+1,right_idx)

    return max(min_squared,left_squared,right_squared)

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



