import sys

a,b,c,d = list(map(int,sys.stdin.readline().split()))

if a-c >1 and b-d >1:
    print(1)
else:
    print(0)