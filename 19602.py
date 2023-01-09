import sys

S  = int(sys.stdin.readline().rstrip())
M  = int(sys.stdin.readline().rstrip())
L  = int(sys.stdin.readline().rstrip())

if (S + 2* M + 3*L) >= 10:
    print("happy")
else:
    print("sad")