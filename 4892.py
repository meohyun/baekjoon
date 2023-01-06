import sys
import math

i = 0
while True:
    i+=1
    n = int(sys.stdin.readline())

    if n ==0:
        break

    n1 = 3*n

    if n1 % 2 == 0:
        n2 = n1 /2
        answer ="even"
    else:
        n2 = (n1+1)/2
        answer = "odd"

    n3 = 3*n2

    n4 = math.floor(n3/9)
    
    print(f"{i}. {answer} {n4}")
    


    