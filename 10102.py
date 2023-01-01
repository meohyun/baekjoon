import sys

V = int(sys.stdin.readline())

result = list(map(str,sys.stdin.readline().strip()))

if result.count("A")> result.count("B"):
    print("A")
elif result.count("A") < result.count("B"):
    print("B")    
else:
    print("Tie")