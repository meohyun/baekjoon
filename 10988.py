import sys
a = 0
word = list(map(str,sys.stdin.readline().strip()))

for i in range(len(word)//2):
    if word[i] == word[len(word)-i-1]:
        a += 1
    else:
        pass

if len(word)//2 == a:
    print(1)
else:
    print(0)
