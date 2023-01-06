import sys


T = int(sys.stdin.readline())
for i in range(T):
    a = 1
    pair = []
    num = int(sys.stdin.readline())

    for a in range(1,num):
        if a < num-a:
            pair.append(a)
            pair.append(num-a)
            a += 1
    
    answer = ""
    for i in range(0,len(pair),2):
        if len(pair) > 0:
            answer += f"{pair[i]} {pair[i+1]}"
        if len(pair) > 2:
            answer += ", "

    answer = answer.rstrip(", ")
    print(f"Pairs for {num}:",answer)
        

    

