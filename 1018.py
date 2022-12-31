import sys

M,N = list(map(int,sys.stdin.readline().split()))

array = [[0]*M for i in range(N)]

for i in range(8):
    line = input().split()
    print(line)
    

# for i in array :
#     for j in i:
#         print(j,end=" ")
#     print()