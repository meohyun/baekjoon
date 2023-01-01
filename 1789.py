import sys
a = []
i = 1
S = int(sys.stdin.readline())

while True:
    S -= i
 
    if S < 0:
        break

    a.append(i)
    i += 1  

print(len(a))