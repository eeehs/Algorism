def solution(n):
    answer = 0
    result = round(n ** (1/2),1) 
    if result * result == float(n):
        answer = 1
    else:
        answer = 2
        
    return answer