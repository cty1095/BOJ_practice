import sys

N, M = map(int,sys.stdin.readline().split())
trees = list(map(int,sys.stdin.readline().split()))

high = max(trees)
low = 0
result = 0

while low <= high:
    mid =(high + low) //2
    remain = 0
    for tree in trees:
        if tree >= mid:
            remain += tree - mid 
    if remain >= M:  #딱맞게 짜름 or 너무 적게 자름
        result = mid
        low = mid +1
    else:   #너무 많이 자름
        high = mid - 1
print(result)