import sys

N = int(sys.stdin.readline())

for i in range(N):
    password = list(sys.stdin.readline().rstrip().strip())

    if len(password) >= 6 and len(password) <=9:
        print("yes")
    else:
        print("no")