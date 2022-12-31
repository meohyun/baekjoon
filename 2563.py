import sys
dic = []
N = int(sys.stdin.readline())

for i in range(3):
    x,y = list(map(int,sys.stdin.readline().split()))
    dic.append([x,y])
    for j in range(1):
        if dic[i][0] - dic[j][0] < 10 and dic[i][0] - dic[j][0] >-10 and dic[i][0] != dic[j][0]:
            print(dic[i][0],dic[j][0])

