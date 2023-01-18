import sys

T = int(sys.stdin.readline())
for i in range(T):
    answer = ""
    idx ,word =list(sys.stdin.readline().split())

    word = list(word.strip()) 

    del word[int(idx)-1]

    for i in word:
        answer+= i
    
    print(answer)
    