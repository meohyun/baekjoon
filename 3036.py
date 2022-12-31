import sys
import math

N = int(sys.stdin.readline())

a = list(map(int,sys.stdin.readline().split()))

for i in range(1,len(a)):
    GCD = math.gcd(a[0],a[i])
    print(f"{a[0]//GCD}/{a[i]//GCD}")