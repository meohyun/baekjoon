import sys
apples = []
bannas = []
A = 0
B = 0
for i in range(3):
    apples.append(int(sys.stdin.readline().rstrip()))
for i in range(3):
    bannas.append(int(sys.stdin.readline().rstrip()))

for i in range(3):
    A += apples[i]*(3-i)
    B += bannas[i]*(3-i)

if A > B:
    print("A")
elif A < B:
    print("B")
else:
    print("T")