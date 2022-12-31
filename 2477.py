import sys 

K = int(sys.stdin.readline())
dics =[]
a = 1
z = []
x =[]
y= []
for i in range(6):
    dic,length = list(map(int,sys.stdin.readline().split()))

    z.append(length)
    # length
    if dic == 1 or dic == 2:
        x.append(length)

    if dic== 3 or dic ==4 :
        y.append(length)

    # dic
    if dic not in dics:
        dics.append(dic)
    else:
        print(z[dics.index(dic)])
    

#print(max(x)*max(y))