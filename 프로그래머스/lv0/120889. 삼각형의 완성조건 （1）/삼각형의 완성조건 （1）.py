def solution(sides):
    answer = 0
    a = sorted(sides)
    if a[2] < a[0] + a[1] :
        answer = 1
    else:
        answer = 2 
    return answer