import sys

while True:
    A,B = list(map(int,sys.stdin.readline().split()))

    if A== 0 and B ==0:
        break
    
    if A > B:
        print("Yes")
    else:
        print("No")