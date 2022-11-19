def solution(my_string):
    answer = 0
    number = "123456789"
    for i in my_string:
        if i in number:
            answer += int(i)
        
    return answer