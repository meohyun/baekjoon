import sys

T = int(sys.stdin.readline())
for i in range(T):
    a,b = list(map(int,sys.stdin.readline().split()))
    print(a+b)