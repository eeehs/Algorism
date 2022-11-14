def solution(age):
    answer = ''
    code = ["a","b","c","d","e","f","g","h","i","j"]
    q = str(age)
    age_list = []
    for i in q:
        age_list.append(i)
    for agee in age_list:
        answer += code[int(agee)]
    return answer