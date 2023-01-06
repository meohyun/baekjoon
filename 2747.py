import sys
a = [0,1]
n = int(sys.stdin.readline())
for i in range(2,n+1):
    
    a.append(a[i-1]+a[i-2])

print(a[-1])