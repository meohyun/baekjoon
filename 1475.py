import sys

N = sys.stdin.readline()
answer = 0
num = []

for i in N:
    num.append(i)

set_num = list(set(num))

for i in set_num:

    if i =="6" or i == "9":
        answer += round(num.count(i)/2)
    else:
        answer += num.count(i)-1

print(answer)


