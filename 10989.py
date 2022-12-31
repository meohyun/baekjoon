import sys

N = int(sys.stdin.readline())

lis=[0]*10001

for i in range(N):
    num = int(sys.stdin.readline())
    lis[num] +=1

for i in range(len(lis)):
    for _ in range(lis[i]):
        print(i)