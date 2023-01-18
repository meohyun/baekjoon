import sys

answer = 0
N = int(sys.stdin.readline())
seat = list(map(int,sys.stdin.readline().split()))

for i in list(set(seat)):
    answer += seat.count(i)-1

print(answer)