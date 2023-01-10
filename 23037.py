import sys
answer = 0
n = list(map(int,sys.stdin.readline().strip()))

for i in n:
    answer += i**5

print(answer)