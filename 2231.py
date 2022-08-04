import sys

N = int(sys.stdin.readline())

for i in range(N):
    num = map(int,str(i))
    result = i + sum(num)
    
    if result == N:
        print(i)
        break
else:
    print(0)

