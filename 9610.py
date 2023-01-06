import sys

n = int(sys.stdin.readline())
axis = 0
q1 = 0
q2 = 0
q3 = 0
q4 = 0

for i in range(n):
    x,y = list(map(int,sys.stdin.readline().split()))

    if x ==0 or y ==0:
        axis += 1
    elif x >0 and y >0:
        q1 +=1
    elif x < 0 and y>0:
        q2 +=1
    elif x < 0 and y<0:
        q3 +=1
    elif x > 0 and y<0:
        q4 +=1

print(f"Q1: {q1}")
print(f"Q2: {q2}")
print(f"Q3: {q3}")
print(f"Q4: {q4}")
print(f"AXIS: {axis}")
