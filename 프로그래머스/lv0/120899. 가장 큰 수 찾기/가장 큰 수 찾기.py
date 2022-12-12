def solution(array):
    answer = []
    new_array = sorted(array)
    big= new_array[len(new_array)-1]
    answer.append(big)
    answer.append(array.index(big))

    return answer