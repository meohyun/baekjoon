import sys

n = int(sys.stdin.readline())
count = 0
while True:
    
    if n % 2 == 0:
        n = n/2
    else:
        n += 1

    count+=1

    if n == 1:
        break
    

print(count)