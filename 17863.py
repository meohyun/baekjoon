import sys

numbers = list(sys.stdin.readline().strip())

if numbers[0] == numbers[1] == numbers[2] == "5":
    print("YES")
else:
    print("NO")
