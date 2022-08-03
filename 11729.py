import sys
def hanoi(n,start,end): # start = 첫번째장대, end = 세번째 장대
    if n ==1:
        print(start,end) # n = 1이면 첫번째 장대에서 세번째 장대으로 한번만 옮기면 됨
    else: # 그 외의 경우
        hanoi(n-1,start,6-start-end) # 첫번째 장대의 n-1개의 원판을 두번째 장대로 옮기고 n번째 원판을 세번째 장대에 놓는다.
        print(start,end) 
        hanoi(n-1,6-start-end,end) # 두번째 장대에 있던 n-1개의 원판을 세번째 장대로 옮기면 끝

n = int(sys.stdin.readline())

print(2**n-1) # 최소 이동 횟수
hanoi(n,1,3)