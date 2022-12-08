def solution(s):
    answer = ''
    s_count = {}
    for i in s:
        if i in s_count:
            s_count[i] +=1
        else:
            s_count[i] = 1
    for i in s_count:
        if s_count[i] == 1:
            answer += i
            answer = "".join(sorted(answer))
    return answer