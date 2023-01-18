import sys

T = int(sys.stdin.readline())
for i in range(T):
    C = int(sys.stdin.readline().rstrip())

    a = C // 25
    b = (C -(a*25))//10
    c = (C-(a*25)-(b*10))//5
    d = (C-(a*25)-(b*10)-(c*5))

    print(a,b,c,d)

    