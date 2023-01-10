import sys

n = int(sys.stdin.readline())

for i in range(n):
    p = int(sys.stdin.readline())
    a = []
    for i in range(p):
        C,name= list(sys.stdin.readline().split())
        a.append([int(C),name])
    a = sorted(a)

    print(a[-1][1])
