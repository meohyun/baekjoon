import sys

A,B  = list(map(int,sys.stdin.readline().split()))
answer =[]
for i in range(A,B+1):
    num = str(i)
    if num.__contains__("0") or num.__contains__("1"):
        pass 
    elif num.__contains__("2") or num.__contains__("3"):
        pass 
    elif num.__contains__("5") or num.__contains__("6"):
        pass 
    elif num.__contains__("8") or num.__contains__("9"):
        pass 
    else:
        answer.append(i) 

print(len(answer))