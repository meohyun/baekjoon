import sys

while True:
    a = []
    n = int(sys.stdin.readline())
    
    if n == -1:
        break

    for i in range(1,n):
        if n % i == 0:
            a.append(i)

    word = f"{n} = {a[0]}"
    
    for i in range(1, len(a)):
        word += " + " + str(a[i])
    
    if sum(a) == n:
        print(word)
    else:
        print(f"{n} is NOT perfect.")

    
