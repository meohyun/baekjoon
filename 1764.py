import sys
count = 0

N,M = list(map(int,sys.stdin.readline().split()))

N_list = [sys.stdin.readline().strip() for i in range(N)]
M_list = [sys.stdin.readline().strip() for i in range(M)]

duplicate = list(set(N_list)&set(M_list))

print(len(duplicate))
for i in sorted(duplicate):
    print(i)
    

   


