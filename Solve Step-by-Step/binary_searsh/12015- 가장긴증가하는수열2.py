import sys

N = int(input())   
listA = list(map(int,sys.stdin.readline().split()))
arr = []
arr.append(listA[0])

for i in range(1,N):

    if listA[i] > arr[-1]:
        arr.append(listA[i])
    else:  #대체 로직
        high = len(arr) -1
        low = 0
        result = 0

        while low <= high:
            mid = (low+high)//2
            if arr[mid] < listA[i]:
                low = mid + 1
            else:
                high = mid -1
        arr[low] = listA[i]
print(len(arr))