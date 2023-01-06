import sys
N = int(sys.stdin.readline())
price = list(map(int,sys.stdin.readline().split()))
index = []
my_price = []

for i in price:
    index.append(price.index(i)+1)

for i in index:
    for j in index:
        if i+j == N:
            my_price.append(price[i-1]+price[j-1])

print(max(my_price))
