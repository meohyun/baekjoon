import sys

A,B,N = list(map(int,sys.stdin.readline().split()))

for i in range(N):
    A = (A % B) * 10
    tmp = A // B

print(tmp)

