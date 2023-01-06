import sys

N,M = list(map(int,sys.stdin.readline().split()))

num = list(map(int,sys.stdin.readline().split()))

# 누적합 
for i in range(N-1):
    num[i+1] += num[i]
num = [0] + num


for i in range(M):
    a,b =list(map(int,sys.stdin.readline().split()))
    print(num[b]-num[a-1])
