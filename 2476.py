import sys

ans = []
N = int(sys.stdin.readline())
for i in range(N):
    a = list(map(int,sys.stdin.readline().split()))

    if a[0]==a[1]==a[2]:
        ans.append(10000+a[0]*1000)
    elif a[0]==a[1]!=a[2]:
        ans.append(1000+a[0]*100)
    elif a[0]!=a[1]==a[2]:
        ans.append(1000+a[1]*100)
    elif a[0]==a[2]!=a[1]:
        ans.append(1000+a[2]*100)
    elif a[0]!=a[1]!=a[2]:
        ans.append(max(a)*100)

print(max(ans))