def solution(my_string, num1, num2):
    answer = ''
    list_string = list(my_string)
    for_num2 = list_string[num1]
    for_num1 = list_string[num2]
    
    list_string[num1] = for_num1
    list_string[num2] = for_num2
    answer = "".join(list_string)
    return answer