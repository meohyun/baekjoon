import sys
answer = ""
name = list(sys.stdin.readline().rstrip().split("-"))

for i in range(len(name)):
    answer += list(name[i].strip())[0]

print(answer)