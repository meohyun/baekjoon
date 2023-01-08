import sys

s = int(sys.stdin.readline())

word = list(sys.stdin.readline().strip())

if word.count('2') == word.count('e'):
    print('yee')
elif word.count('2') > word.count('e'):
    print('2')
else:
    print("e")


