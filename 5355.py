import sys

T = int(sys.stdin.readline())
for i in range(T):

    a = list(sys.stdin.readline().split())
    ans = float(a[0])
    for i in range(1,len(a)):
        if a[i] == "@":
            ans*=3 
        if a[i] == "%":
            ans+=5
        if a[i] == "#":
            ans-=7
    
    print(format(ans,'.2f'))