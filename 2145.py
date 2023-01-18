import sys
while True:
    N = int(sys.stdin.readline())

    if N == 0:
        break
    
    while (N>9):
        N = sum(map(int,list(str(N))))

    print(N)
    

    




    
