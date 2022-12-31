import sys

N = int(sys.stdin.readline())
num = []

for i in range(N):
    n = int(sys.stdin.readline())
    num.append(n)

num = sorted(num)

for i in range(N):
    print(num[i])