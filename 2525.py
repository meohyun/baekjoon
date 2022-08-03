import sys 

A,B = map(int,sys.stdin.readline().split())
C = int(sys.stdin.readline())

hour = C // 60
min= C % 60 
end_hour = A+hour+(B+min)//60

if end_hour >= 24:
    end_hour -= 24

if B + min >= 60:
    print(end_hour,B+min-60)
else:
    print(end_hour,B+min)


