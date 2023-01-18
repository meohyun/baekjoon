import sys
answer = 0
a = 0
N = int(sys.stdin.readline())

num = list(map(int,sys.stdin.readline().split()))

for i in num:
    if i == 1:
        a += 1
        answer += a
    else:
        a = 0

print(answer)
        