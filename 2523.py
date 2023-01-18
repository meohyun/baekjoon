import sys

N = int(sys.stdin.readline())

for i in range(1,N+1):
    answer = ""
    answer += "*"*i
    print(answer)
for i in range(1,N):
    answer = ""
    answer += "*"*(N-i)
    print(answer)