def solution(my_string):
    answer = ''
    moim = "aeiou"
    
    for i in my_string:
        if i in moim:
            my_string = my_string.replace(i,"")
    answer = my_string
    return answer