import sys

N = int(sys.stdin.readline())

blank = " "

for i in range(N):
    answer =""
    answer += (blank * i) + ("*"*(N-i))
    print(answer)

