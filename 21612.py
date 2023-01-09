import sys

B = int(sys.stdin.readline())
kpa = B*5-400
print(kpa)

if kpa > 100 :
    print(-1)
if kpa == 100:
    print(0)
if kpa < 100:
    print(1)