import sys

while True:
    a,b = list(map(int,sys.stdin.readline().split()))

    if a == 0:
        break

    if a % b == 0:
        print("multiple")
    elif b % a == 0:
        print("factor")
    else:
        print("neither")
