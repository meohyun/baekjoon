import sys
c = []
d = []
for i in range(3):
    a,b= list(map(int,sys.stdin.readline().split()))
    if a not in c:
        c.append(a)
    else:
        del c[c.index(a)]
    if b not in d:
        d.append(b)
    else:
        del d[d.index(b)]

print(c[0],d[0])

