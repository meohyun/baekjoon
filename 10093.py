import sys
num = []
A,B = list(map(int,sys.stdin.readline().split()))

if A < B : 
    for i in range(A+1,B):
        num.append(i)
else:
    for j in range(B+1,A):
        num.append(j)

print(len(num))
for i in num:
    print(i,end=" ")