import sys

num = int(sys.stdin.readline())

div = list(map(int,sys.stdin.readline().split()))

print(max(div)*min(div))