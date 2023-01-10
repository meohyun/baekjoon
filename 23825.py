import sys

N,M = list(map(int,sys.stdin.readline().split()))

if N//2 ==  M//2:
    print(N//2) 
elif N//2 > M//2:
    print(M//2)
else:
    print(N//2)