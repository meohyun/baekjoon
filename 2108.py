import sys
from collections import Counter

N = int(sys.stdin.readline())
n=[]

for i in range(N):
    n.append(int(sys.stdin.readline()))

n = sorted(n)
cnt = Counter(n)
p = cnt.most_common(N)

print(round(sum(n)/N),n[N//2],sep='\n')
if N > 1:
    if p[0][1] == p[1][1]:
        print(p[1][0])
    else:
        print(p[0][0])
if N == 1:
    print(p[0][0])
print(n[N-1]-n[0])