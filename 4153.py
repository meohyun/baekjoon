import sys 

for i in range(30000):
    a,b,c = list(map(int,sys.stdin.readline().split()))

    if a==b==c==0:
        break

    if a**2 + b**2 == c**2:
        print("right")
    elif a**2 + c**2 == b**2:
        print("right")
    elif b**2 + c**2 == a**2:
        print("right")    
    else:
        print("wrong")

    
