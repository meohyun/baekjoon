import sys

N,K = list(map(int,sys.stdin.readline().split()))
num = list(map(int,sys.stdin.readline().split()))

for i in range(N-1):
    num[i] = num[i]+num[i+1]


print(num)