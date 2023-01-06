import sys

T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    school = []
    Liter = []
    for j in range(N):
        S,L = list(sys.stdin.readline().split())
        school.append(S)
        Liter.append(int(L))

    print(school[Liter.index(max(Liter))])