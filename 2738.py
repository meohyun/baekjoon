import sys
x = []
y = []
plus = []
N,M = list(map(int,sys.stdin.readline().split()))

for i in range(N):
    x.append(list(map(int,sys.stdin.readline().split())))

for i in range(N):
    y.append(list(map(int,sys.stdin.readline().split())))
    for j in range(M):
        y[i][j] = x[i][j] +y[i][j]     

for i in y:
    for j in i:
        print(j,end=" ")       
    print()  
