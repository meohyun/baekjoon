import sys

count = 0
for _ in range(6):
    
    result = sys.stdin.readline().rstrip()

    if result =="W":
        count +=1
    
if count >=5:
    print(1)
elif count == 3 or count ==4:
    print(2)
elif count ==2 or count ==1:
    print(3)
else:
    print(-1)