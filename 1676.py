import sys

N = int(sys.stdin.readline())
answer = 1
count = 0
for i in range(N,1,-1):
    answer *=i

num = str(answer).strip()

for i in range(-1,-(len(num)+1),-1):
    if num[i]== "0":
        count+=1
    else:
        break
print(count)
