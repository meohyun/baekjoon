import sys
import datetime

x,y = list(map(int,sys.stdin.readline().split()))

dt = datetime.datetime(2007,x,y)
answer= dt.weekday()

if answer == 0:
    print("MON")
if answer == 1:
    print("TUE")
if answer == 2:
    print("WED")
if answer == 3:
    print("THU")
if answer == 4:
    print("FRI")
if answer == 5:
    print("SAT")
if answer == 6:
    print("SUN")