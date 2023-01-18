import sys

T = int(sys.stdin.readline())

for i in range(T):
    answer = 0
    sum = 1
    n = int(sys.stdin.readline())

    for i in range(1,n+1):
        sum += i+1
        answer += i*sum
    
    print(answer)
