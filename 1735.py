import sys
import math

A,B = list(map(int,sys.stdin.readline().split()))
C,D = list(map(int,sys.stdin.readline().split()))

answer_b = math.lcm(B,D)

answer_a = A*(answer_b//B) + C*(answer_b//D)

if math.gcd(answer_b,answer_a) != 1:
    a = answer_a // math.gcd(answer_b,answer_a)
    b = answer_b // math.gcd(answer_b,answer_a)
else:
    a = answer_a
    b = answer_b

print(a,b)


