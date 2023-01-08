import sys
nums=[]
answer = 0
num = sys.stdin.readline().rstrip()

for i in num:
    if i == "A":
        i = 10
    if i == "B":
        i = 11
    if i == "C":
        i = 12
    if i == "D":
        i = 13
    if i == "E":
        i = 14
    if i == "F":
        i = 15

    nums.append(i)

for i in range(len(nums)):
    
    answer += int(nums[i]) * 16**(len(nums)-(i+1))

print(answer)

# 16진수 > 10진수
# 10 > 16
# 11 > 17
# 12 > 18