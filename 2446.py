import sys

N = int(sys.stdin.readline())
blank = " "
for i in range(1,N+1):
    answer =""
    answer += blank *(i-1) + "*"*(((N-(i-1))*2)-1) 
    print(answer)

for i in range(1,N):
    answer =""
    answer += blank *(N-(i+1)) + "*"*((2*(i+1))-1)
    print(answer)

