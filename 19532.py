num = list(map(int, input().split()))

if num[1] == 0:
    x = num[2] / num[0]
    y = (num[5] - num[3] * x) / num[4]
    
elif num[4] == 0: 
    x = num[5] / num[3]
    y = (num[2] - num[0] * x) / num[1]
else:
    tmp_0 = num[0] / num[1]
    tmp_3 = num[3] / num[4]
    tmp_2 = num[2] / num[1]
    tmp_5 = num[5] / num[4]

    a = tmp_0 - tmp_3
    b = tmp_2 - tmp_5
    x = b / a
    y = (num[2] - num[0] * x) / num[1]
print(round(x), round(y))
