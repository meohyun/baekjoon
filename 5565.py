import sys

sum = int(sys.stdin.readline().rstrip())
answer = 0
for i in range(9):
    a = int(sys.stdin.readline().rstrip())
    answer += a

print(sum-answer)
