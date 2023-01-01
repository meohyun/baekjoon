import sys

score = list(map(str,sys.stdin.readline().strip()))

if score[0] == "A":
    score[0]= 4.0
elif score[0] == "B":
    score[0]= 3.0
if score[0] == "C":
    score[0]= 2.0
if score[0] == "D":
    score[0]= 1.0
if score[0] == "F":
    score[0]= 0.0
    score.append("*")
    

if score[1] =="0":
    print(score[0])
elif score[1] =="+":
    print(score[0]+0.3)
elif score[1] =="-":
    print(score[0]-0.3)
else:
    print(score[0])


