import sys

X,Y = list(sys.stdin.readline().split())
x = []
y =[]
answer_x = ""
answer_y = ""
a = []
real_answer =""
for i in X:
    x.append(i)

for i in Y:
    y.append(i)

for i in range(len(x)):
    answer_x += x[len(x)-(i+1)]

for i in range(len(y)):
    answer_y += y[len(y)-(i+1)]

answer = int(answer_x)+int(answer_y)
answer = str(answer)

for i in answer:
    a.append(i)

for i in range(len(a)):
    real_answer += a[len(a)-(i+1)]

print(int(real_answer))