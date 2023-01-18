import sys
N = int(sys.stdin.readline().rstrip())
count = 0
answer = ""

while True:
    if N < 10:
        break
    n = []

    for i in str(N):
        n.append(int(i))
    
    N = sum(n)

    count +=1


if N % 3 == 0:
    answer = "YES"
else:
    answer = "NO"
    
print(count)
print(answer)
    