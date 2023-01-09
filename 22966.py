import sys

N = int(sys.stdin.readline())
a = []
b = []

for i in range(N):
    title,num = list(sys.stdin.readline().split())
    a.append(title)
    b.append(num)


for i in range(N):
    if b[i] == min(b):
        print(a[b.index(b[i])])
    


   