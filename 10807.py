import sys
count = 0
N = int(sys.stdin.readline())

a = list(map(int,sys.stdin.readline().split()))

v = int(sys.stdin.readline())

for i in a:
    if i== v:
        count+=1

print(count)