import sys
N = int(sys.stdin.readline())

for i in range(N):
    r,e,c = list(map(int,sys.stdin.readline().split()))

    if e-c > r:
        print("advertise")
    elif e-c == r:
        print("does not matter")
    else:
        print("do not advertise")