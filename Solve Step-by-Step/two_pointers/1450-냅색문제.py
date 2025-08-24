def subset_sum(items):
    sums =[0]
    L = len(items)
    for i in range(L):
        tmp = []
        for sum in sums:
            new = items[i] + sum
            tmp.append(new)
        sums += tmp

    sums.sort()
    return sums

def two_point(sumL,sumR,C):
    left = 0
    right = len(sumR) - 1 
    cnt = 0
    while True:
        if left >= len(sumL):
            return cnt
        if right == -1:
            return cnt
        
        sumLR = sumL[left] + sumR[right]
        if sumLR <= C:
            cnt += (right+1)
            left += 1
        elif sumLR > C:
            right -= 1

N, C = map(int,input().split())

items = list(map(int,input().split()))

itemL = items[:(N//2)]
itemR = items[(N//2):]

# print(itemL)
# print(itemR)

sumL = subset_sum(itemL)
sumR = subset_sum(itemR)

# print(sumL)
# print(sumR)

result = two_point(sumL,sumR,C)
print(result)