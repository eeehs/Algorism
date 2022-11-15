def solution(hp):
    answer = 0
    a = hp // 5
    b = (hp % 5) // 3 
    c = ((hp % 5) % 3) // 1 
    answer = a + b + c
    return answer