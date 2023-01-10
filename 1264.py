import sys

a = ['a','e','i','o','u']

while True:
    count = 0
    sen = list(sys.stdin.readline().rstrip().strip())

    if sen[0] == "#":
        break

    for i in range(len(sen)):
        if sen[i].lower() in a :
            count+=1
    
    print(count)