def solution(array, n):
    answer = 0
    array.append(n)
    array = sorted(array)
    n_index = array.index(n)
    if  array[n_index] == array[0]:
        answer = array[1]
    elif array[n_index] == array[len(array)-1]:
        answer = array[n_index-1]
    elif n - array[n_index -1] < array[n_index + 1] - n:
        answer = array[n_index -1]
    elif n - array[n_index -1] > array[n_index + 1] - n:
        answer = array[n_index + 1]
    else:
        answer = array[n_index - 1]
    return answer
