import sys
num = []
N,K = list(map(int,sys.stdin.readline().split()))

for i in range(1,N+1):
    if N % i == 0:
        num.append(i)

if len(num) >= K:
    print(num[K-1])
else:
    print(0)