import sys

num = list(map(int,sys.stdin.readline().split()))

num = sorted(num)

for i in num:
    print(i,end=" ")