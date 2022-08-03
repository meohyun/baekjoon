import sys

A,B,C = num =list(map(int,sys.stdin.readline().split()))

if A == B == C:
    print(10000+A*1000)

if A == B != C:
    print(1000+A*100)

if A != B == C:
    print(1000+B*100)

if A == C != B:
    print(1000+A*100)

if A != B and B!= C and A!=C:
    print(max(num)*100)

