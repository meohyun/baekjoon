import sys

N = int(sys.stdin.readline())

a = []

for i in range(N):
    x,y = list(map(int,sys.stdin.readline().split()))
    a.append([x,y])
    
for i in range(len(a)):
    rank = 1
    for j in range(len(a)): 
        if a[i][0] < a[j][0] and a[i][1] < a[j][1]:
            rank += 1
    print(rank)






