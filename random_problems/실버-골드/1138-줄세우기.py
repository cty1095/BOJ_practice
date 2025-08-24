import sys
input = sys.stdin.readline

N =  int(input())

arr = list(map(int,input().split()))
height= [] 

for i in range(N-1,-1,-1):
    idx = arr[i]
    height.insert(idx,i+1)
print(*height)