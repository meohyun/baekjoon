import sys

T = int(sys.stdin.readline())
for i in range(T):
    answer= 0
    num = list(map(int,sys.stdin.readline().strip().rstrip()))
    
    for i in range(len(num)):
        answer += num[i] * 2**(len(num)-(i+1))
        
    print(answer)
