import sys
isbn =[]
answer= 0
for i in "9780921418":
    isbn.append(int(i))

for i in range(3):
    isbn.append(int(sys.stdin.readline().rstrip()))

for i in range(len(isbn)):
    if i% 2 == 0:
        answer += isbn[i]*1
    else:
        answer += isbn[i]*3

print(f"The 1-3-sum is {answer}")