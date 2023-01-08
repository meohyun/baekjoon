import sys

n = int(sys.stdin.readline())
for i in range(n):
    answer = "="
    k = int(sys.stdin.readline().rstrip())
    answer *= k
    
    print(answer)
