import sys

while True:
    word = list(sys.stdin.readline().rstrip().strip())
    count = 0
    for i in range(len(word)):
        if word[i] == word[len(word)-(i+1)]:
            count +=1

    if word[0] == "0":
        break

    if count == len(word):
        print("yes")
    else:
        print("no")
