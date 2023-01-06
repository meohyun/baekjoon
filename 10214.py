import sys

T = int(sys.stdin.readline())

for i in range(T):
    y = 0
    k = 0 
    for j in range(9):
        Y,K = list(map(int,sys.stdin.readline().split()))
        y+=Y
        k+=K
    
    if y> k:
        print("Yonsei")
    elif y<k:
        print("Korea")
    else:
        print("Draw")