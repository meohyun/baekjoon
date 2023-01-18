import sys

T = int(sys.stdin.readline())
alp = [" ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
for i in range(T):
    answer = ""
    num = []
    message = list(sys.stdin.readline().strip())

    for i in message:
        num.append(alp.index(i))

    rule = list(sys.stdin.readline().strip())
    rule.append(" ")

    for i in range(len(message)):
        answer += rule[num[i]-1]
    
    print(answer)
    
