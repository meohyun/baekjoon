import sys

n = int(sys.stdin.readline())
a = 100
b = 100

for i in range(n):
    A,B = list(map(int,sys.stdin.readline().split()))

    if A > B :
        b-= A
    elif A < B:
        a-= B
    else:
        pass

print(a)
print(b)