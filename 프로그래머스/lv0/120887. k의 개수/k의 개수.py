def solution(i, j, k):
    result = list(map(str,range(i,j+1)))
    str_result = "".join(result)
    answer = str_result.count(str(k))
    return answer