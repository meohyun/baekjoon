import sys 
count = 0
T = int(sys.stdin.readline())

answer = list(map(int,sys.stdin.readline().split()))

for i in answer:
    if i == T:
        count+=1 

print(count)