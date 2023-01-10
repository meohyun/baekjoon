import sys

word = sys.stdin.readline().rstrip()
split_word = list(word.strip())

answer = ""
for i in range(len(split_word)):
    if i % 10 == 0 and i !=0:
        answer += "\n"
    answer+=split_word[i]
    
print(answer)

    


