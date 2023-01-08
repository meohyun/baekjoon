import sys

L = int(sys.stdin.readline())

for i in range(L):
    N,mes = list(sys.stdin.readline().split())

    print(mes*int(N))