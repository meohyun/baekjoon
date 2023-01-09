import sys
n = int(sys.stdin.readline())
prize = list(map(int,sys.stdin.readline().split()))

if sum(prize) % 3 == 0:
    print("yes")
else:
    print("no")