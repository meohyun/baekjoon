import sys
num = []
a,b = list(map(int,sys.stdin.readline().split()))
c,d = list(map(int,sys.stdin.readline().split()))

num.append([a/c,b/d])
num.append([c/d,a/b])
num.append([d/b,c/a])
num.append([b/a,d/c])

answer = []
for i in range(4):
    answer.append(sum(num[i]))

print(answer.index(max(answer)))

