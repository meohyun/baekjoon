import sys
import datetime

now = datetime.datetime.now()

a,b,c = list(map(int,sys.stdin.readline().split(":")))
d,e,f = list(map(int,sys.stdin.readline().split(":")))

first_time = now.replace(hour=a,minute=b,second=c)
second_time =now.replace(hour=d,minute=e,second=f)

a = str(second_time-first_time).split(', ')


# 시간이 0일경우 0만 출력되어 lambda를 사용하여 0을 앞에 붙여줘야함
if len(a) >= 2:
    print((lambda x: '0'+x if len(x) < 8 else x)(a[1]))
else:
    print((lambda x: '0'+x if len(x) < 8 else x)(a[0]))

