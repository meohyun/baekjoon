import sys
a = [0,1]
n = int(sys.stdin.readline())

for i in range(n):
    a.append(a[i]+a[i+1])

print(a[-2])