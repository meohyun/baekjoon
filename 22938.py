import sys

x1,y1,r1 = list(map(int,sys.stdin.readline().split()))
x2,y2,r2 = list(map(int,sys.stdin.readline().split()))

side = ((x1-x2)**2+(y1-y2)**2)**0.5
if r1 + r2 > side:
    print("YES")
else:
    print("NO")
