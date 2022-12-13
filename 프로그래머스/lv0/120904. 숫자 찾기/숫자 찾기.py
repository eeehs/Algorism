def solution(num, k):
    str_num = str(num)
    str_k = str(k)
    answer = 0
    if str_k in str_num:
        answer = str_num.index(str_k)+1
    else:
        answer = -1
    return answer