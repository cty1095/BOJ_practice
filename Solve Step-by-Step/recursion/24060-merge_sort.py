order = []

def merge_sort(lst):
    if len(lst) <= 1:
        return lst, 0
    
    mid = len(lst) // 2

    left = lst[:mid]
    right = lst[mid:]
    
    left_sorted, cnt_left = merge_sort(left)
    right_sorted, cnt_right = merge_sort(right)
    sorted_list, cnt_merge = merge(left_sorted, right_sorted)
    cnt_total = cnt_left + cnt_merge + cnt_right
    return sorted_list, cnt_total

def merge(left, right):
    global order
    result = []
    i = j = 0
    cnt = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            order.append(left[i])
            i += 1
        else:
            result.append(right[j])
            order.append(right[j])
            j += 1
        cnt += 1

    while i < len(left):
        result.append(left[i])
        order.append(left[i])
        i += 1
        cnt += 1

    while j < len(right):
        result.append(right[j])
        order.append(right[j])
        j += 1
        cnt += 1

    return result, cnt

N, K = map(int, input().split())
listA = list(map(int, input().split()))

order.clear()

sorted_listA, cnt = merge_sort(listA)

if K <= len(order):
    print("order : ", order )
    print(order[K-1])
    print("sorted list : ", sorted_listA)
else:
    print(-1)


