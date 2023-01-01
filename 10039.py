import sys 

a = []
for i in range(5):

    A = int(sys.stdin.readline())

    if A <40 :
        A = 40
    a.append(A)

print(sum(a)//5)