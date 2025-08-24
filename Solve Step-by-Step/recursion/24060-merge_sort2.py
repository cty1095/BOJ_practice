order = []

def merge_sort(list,start,end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(list, start, mid)
        merge_sort(list, mid + 1, end)
        merge(list,start,mid,end)

def merge(list,start,mid,end):        
    global order
    i = start
    j = mid + 1
    tmp = []

    while i <= mid and j <= end:
        if list[i] <= list[j]:
            tmp.append(list[i])
            order.append(list[i])
            i += 1
        else:
            tmp.append(list[j])
            order.append(list[j])
            j += 1
    while i <= mid:
        tmp.append(list[i])
        order.append(list[i])
        i += 1
    while j <= end:
        tmp.append(list[j])
        order.append(list[j])
        j += 1
    i = start
    t = 0
    while i <= end:
        list[i] = tmp[t]
        i += 1
        t += 1
    



N, K = map(int,input().split())
listA = list(map(int,input().split()))
merge_sort(listA,0,N-1)

# print(order)
if K <= len(order):
    print(order[K-1])
else:
    print(-1)
