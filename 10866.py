import sys

N = int(sys.stdin.readline())
o = []
for i in range(N):
    a = int(sys.stdin.readline())
    o.append(a)

if o.count(0) > o.count(1):
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")
