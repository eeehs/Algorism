def solution(array):
    answer = 0
    re = 0
    result = {}
    for i in array:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    for i in result:
        if result[i] > re:
            answer = i
            re = result[i]
        elif result[i] == re:
            answer = -1
    return answer