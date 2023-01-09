import sys

K,D,A = list(map(int,sys.stdin.readline().split('/')))

if K + A < D or D ==0:
    print("hasu")
else:
    print("gosu")
    