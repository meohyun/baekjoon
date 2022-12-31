import sys

N = int(sys.stdin.readline())
num = []

for i in range(N):
    n = int(sys.stdin.readline())
    num.append(n)

for i in range(N):
    for j in range(i+1,N):
        if num[i] > num[j]:
            p = num[i]
            num[i] = num[j]
            num[j] = p
    print(num[i])