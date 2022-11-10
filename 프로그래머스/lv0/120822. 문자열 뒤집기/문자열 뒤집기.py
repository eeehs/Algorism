def solution(my_string):
    answer = []
    list_my = list(my_string)
    for i in range(len(list_my)):
        answer.insert(0,list_my[i])
    answer = "".join(answer)
    return answer