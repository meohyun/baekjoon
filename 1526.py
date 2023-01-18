import sys

N = int(sys.stdin.readline())
answer = []

for i in range(1,N+1):
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
    
print(max(answer))