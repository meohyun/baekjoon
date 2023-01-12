import sys

A,B = list(sys.stdin.readline().split())
answer = 0
c = 0
for i in B:
    c += int(i)
    
for i in A:
    answer += int(i)*c

print(answer)