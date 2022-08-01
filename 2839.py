import sys

N = int(sys.stdin.readline())
a = []

for A in range(N):
    for B in range(N):
        if N == 3*A+5*B:
            a.append([A,B])

if len(a) == 0:
    print(-1)
else:
    print(a[0][0]+a[0][1])
