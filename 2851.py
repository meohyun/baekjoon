import sys

num = []
abs_num = []
answer = 0

for i in range(10):
    a = int(sys.stdin.readline().rstrip())
    answer += a
    num.append(answer-100)
    abs_num.append(abs(answer-100))

a = min(abs_num)

if abs_num.count(a) == 2:
    print(num[abs_num.index(a)+1]+100)
else:
    print(num[abs_num.index(a)]+100)       