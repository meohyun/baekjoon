import sys
n = int(sys.stdin.readline())

num = [0,1]

for i in range(2,n+1):
    num.append(num[i-1]+num[i-2])

if n != 0:
    print(num[-1])
else:
    print(0)

