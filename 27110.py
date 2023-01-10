import sys

N = int(sys.stdin.readline())

num = list(map(int,sys.stdin.readline().split()))
answer =0
for i in range(3):
    if num[i] < N:
        answer += num[i]
    else:
        answer += N

print(answer)