import sys

a,b = list(map(int,sys.stdin.readline().split()))

c = a * ((100-b)/100)

if c >= 100:
    print(0)
else:
    print(1)
