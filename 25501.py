import sys

def recursion(s, l, r):
    global count
    if l >= r:
        return 1
    elif s[l] != s[r]: 
        return 0
    else:
        count+=1
        return recursion(s, l+1, r-1)


def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

T = int(sys.stdin.readline())

for i in range(T):
    count = 1
    test = [i for i in list(sys.stdin.readline().strip())]

    print(isPalindrome(test),count)
