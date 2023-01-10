import sys
import datetime

n = int(sys.stdin.readline())
now = datetime.datetime.now()
answer = []

for i in range(n):
    name,d,m,y = list(sys.stdin.readline().split())
    birthday = now.replace(int(y),int(m),int(d))
    ages = (now - birthday).days
    
    answer.append([name,ages])

    answer = sorted(answer,key=lambda x:x[1])

print(answer[0][0])
print(answer[-1][0])


