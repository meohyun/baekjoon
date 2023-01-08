import sys

N = int(sys.stdin.readline())
score = []
for i in range(N):
    score.append(int(sys.stdin.readline().rstrip()))

if score[0] == max(score):
    print("S")
else:
    print("N")