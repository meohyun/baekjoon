import sys

N = int(sys.stdin.readline())
a = []
answer= ""
for i in range(N):
    name = list(sys.stdin.readline().rstrip().strip())

    a.append(name[0])
    
    set_a = list(set(a))
    set_a = sorted(set_a)

for i in set_a:
    if a.count(i)>=5:
        answer+= i

if answer == "":
    print("PREDAJA")
else:
    print(answer)


