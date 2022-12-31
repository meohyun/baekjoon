import sys

h,m,s = map(int,sys.stdin.readline().split())
D = int(sys.stdin.readline())

a = D // 3600 
b = (D - a * 3600) // 60 
c = (D-  (a* 3600) - (b * 60)) 

ans_h = a+h
ans_m = b+m
ans_s = c+s

if ans_s >=60:
    ans_m +=1
    ans_s -=60
if ans_m >=60:
    ans_h +=1
    ans_m -=60
if ans_h >= 24:
    ans_h = ans_h % 24

print(ans_h,ans_m,ans_s)