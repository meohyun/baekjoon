import sys
from functools import reduce

N = int(sys.stdin.readline())

first_sen ='어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.'

answer = '"재귀함수가 뭔가요?"'

sentence_1_a = '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'
sentence_1_b = '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.'
sentence_1_c = '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'

sentence_2 = '"재귀함수는 자기 자신을 호출하는 함수라네"'

sentence_3 = '라고 답변하였지.'

print(first_sen)
for i in range(N+1):
    print(i*'____'+answer)
    if i < N :
        print(i*'____'+sentence_1_a)
        print(i*'____'+sentence_1_b)
        print(i*'____'+sentence_1_c)
    else:
        print(i*'____'+sentence_2)
        for j in range(N,-1,-1):
            print(j*'____'+sentence_3)



