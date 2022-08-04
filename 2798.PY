import sys

N,M = list(map(int,sys.stdin.readline().split()))

num = list(map(int,sys.stdin.readline().split()))

max = 0
for a in range(N-2):
    for b in range(a+1,N-1):
        for c in range(b+1,N):
            sum = num[a]+num[b]+num[c]
            if (sum > max and sum <= M):
                max = sum

print(max)


