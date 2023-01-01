import sys

A = list(map(str,sys.stdin.readline().strip()))

ans= 10

for i in range(1,len(A)):
    if A[i-1] == A[i]:
        ans+=5
    else:
        ans+=10

print(ans)
        