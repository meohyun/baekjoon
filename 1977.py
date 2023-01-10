import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
n = []

for i in range(M,N+1):
    if i//i**0.5 == i**0.5:
        n.append(i)

if len(n) != 0:
    print(sum(n))
    print(n[0])
else:
    print(-1)