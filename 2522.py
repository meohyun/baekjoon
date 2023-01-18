import sys

N = int(sys.stdin.readline())
blank = " "
for i in range(1,N+1):
    answer = ""
    answer += blank*(N-i) + "*"*i
    print(answer)

for i in range(1,N):
    answer = ""
    answer += blank*i + "*"*(N-i)
    print(answer)
