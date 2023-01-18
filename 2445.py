import sys

N = int(sys.stdin.readline())
blank =" "

for i in range(1,N+1):
    answer = ""
    answer += "*"*i + blank *((N-i)*2)+ "*"*i
    print(answer)

for i in range(1,N):
    answer = ""
    answer += "*"*(N-i) + blank *(i*2)+ "*"*(N-i)
    print(answer)