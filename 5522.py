import sys
num = []
for i in range(5):
    num.append(int(sys.stdin.readline().rstrip()))

print(sum(num))