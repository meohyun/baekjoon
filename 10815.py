N = int(input())

my_num = list(map(int,input().split()))

M = int(input())

num = list(map(int,input().split()))

my_dict= {num[i] :0 for i in range(len(num))}

for i in range(N):
    if my_num[i] in my_dict.keys():
        my_dict[my_num[i]] += 1

print(" ".join(map(str, list(my_dict.values()))))