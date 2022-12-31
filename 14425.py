N,M =map(int,input().split())
S = set()
count = 0

for i in range(N):
    S.add(input())

for _ in range(M):
    t = input()
    if t in S:
        count+=1

print(count)