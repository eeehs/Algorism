def solution(rsp):
    answer = ''
    rsps = list(rsp)
    for i in rsps:
        if i == "2":
            answer += "0"
        elif i =="0":
            answer += "5"
        else:
            answer += "2"
    
    return answer