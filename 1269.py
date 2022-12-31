import sys

A,B = list(map(int,sys.stdin.readline().split()))

A_list = list(map(int,sys.stdin.readline().split()))
B_list = list(map(int,sys.stdin.readline().split()))

print(len(list(set(A_list)-set(B_list)))+len(list(set(B_list)-set(A_list))))
