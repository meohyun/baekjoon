import sys

N = int(sys.stdin.readline())

a = list(map(int,sys.stdin.readline().split()))

M = int(sys.stdin.readline())

b = list(map(int,sys.stdin.readline().split()))

for i in b:
    print(a.count(i),end=" ")
    