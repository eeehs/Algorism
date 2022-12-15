def solution(array):
    answer = 0
    seven = "".join(map(str,array))
    for i in seven:
        if i == "7":
            answer +=1
    return answer