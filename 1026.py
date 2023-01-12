import sys
answer= 0
N = int(sys.stdin.readline())

A = list(map(int,sys.stdin.readline().split()))
B = list(map(int,sys.stdin.readline().split()))

A = sorted(A)
B = sorted(B,reverse=True)

for i in range(len(A)):
    answer += A[i]*B[i]
print(answer)