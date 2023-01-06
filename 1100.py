import sys

chess = []
count = 0
for i in range(8):
    chess.append(list(map(str,sys.stdin.readline().strip())))
    for j in range(8):
        if i % 2 == 0 and j % 2== 0:
            if chess[i][j] =="F":
                count+= 1
        elif i % 2 == 1 and j % 2 == 1:
            if chess[i][j] =="F":
                count+= 1        

print(count)

