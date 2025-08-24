import sys
input = sys.stdin.readline

X = int(input()) 
X = bin(X)
print(X.count('1'))