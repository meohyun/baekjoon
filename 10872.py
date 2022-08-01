import sys
from functools import reduce
N = int(sys.stdin.readline())
num = []

for i in range(1,N+1):
    num.append(i)

def multiply(num):
    return reduce(lambda x, y: x * y, num)

if N != 0 :
    print(multiply(num))
else:
    print(1)
        