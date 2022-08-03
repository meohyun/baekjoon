import sys

def star(n):
    if n == 3:
        return ['***','* *', '***']
    
    else:
        star_list = star(n//3)
        a = []
        
        for i in star_list:
            a.append(i*3) #전 패턴을 각각 3개씩 늘림
            
        for i in star_list:
            a.append(i + " "*(n//3) + i) #공백 추가
                    
        for i in star_list:
            a.append(i*3)
        
        return a

N = int(sys.stdin.readline())
print("\n".join(star(N)))