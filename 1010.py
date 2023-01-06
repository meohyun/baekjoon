import sys

T = int(sys.stdin.readline())

for i in range(T):
    a = 1
    b = 1
    N,M = list(map(int,sys.stdin.readline().split()))


    for i in range(N):
        a *= M-i
        b *= N-i

    print(a//b)