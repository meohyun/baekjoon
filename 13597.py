import sys

a,b = list(map(int,sys.stdin.readline().split()))

if a != b:
    print(max(a,b))
else:
    print(a)