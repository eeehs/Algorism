def solution(order):
    answer = 0
    order = list(str(order))
    for i in order:
        if int(i) !=0 and int(i) % 3 ==0:  
            answer +=1
        else:
            pass
    return answer