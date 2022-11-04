def solution(array):
    answer = 0
    array.sort()
    i = (len(array)+1) // 2 - 1
    answer = array[i]
    return answer