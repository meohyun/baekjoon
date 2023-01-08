import sys
S = int(sys.stdin.readline())
vowels = ['A','E','I','O','U','a','e','i','o','u']

for i in range(S):
    count = 0
    blank_count = 0
    sen = list(map(str,sys.stdin.readline().strip().rstrip()))

    blank_count = sen.count(" ")
    for i in sen:
        if i in vowels:
            count+=1
    print(len(sen)-blank_count-count,count)