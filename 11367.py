import sys
n = int(sys.stdin.readline())

for i in range(n):
    name, score = list(sys.stdin.readline().split())
    score = int(score)
    grade = ""

    if score >=97:
        grade = "A+"
    elif score >= 90:
        grade = "A"
    elif score >= 87:
        grade = "B+"
    elif score >= 80:
        grade = "B"
    elif score >= 77:
        grade = "C+"
    elif score >= 70:
        grade = "C"
    elif score >= 67:
        grade = "D+"
    elif score >= 60:
        grade = "D"
    elif score < 60:
        grade = "F"
    
    print(name,grade)
