K = int(input())

a, b, c, d =map(int,input().split())

left = (a * K) + b
right = (c * K) + d

# print(left)
# print(right)

if left == right:
    print('Yes', left)
else:
    print('No')