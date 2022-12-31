import sys
import math

a,b = list(map(int,sys.stdin.readline().split()))

print(math.gcd(a,b))
print(math.lcm(a,b))