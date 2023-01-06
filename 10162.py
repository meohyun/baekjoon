import sys

T = int(sys.stdin.readline())
a = 0
b = 0
c = 0 
ans = 0

if T >= 300:
    a = T // 300
    b = (T -(a*300))//60
    c = (T-(a*300)-(b*60))//10
    ans = (T-(a*300)-(b*60)-(c*10))
    
elif T >= 60:
    b = T // 60
    c = (T-(b*60))//10
    ans = (T-(b*60)-(c*10))
else:
    c = T // 10
    ans = T-(c*10)


if ans == 0:
    print(a,b,c)
else:
    print(-1)