def solution(numbers, direction):
    answer = []
    n = 0
    for i in range(len(numbers)):
        answer.append("_")
    if direction == "right":
        for num in numbers:
            answer[n+1] = num
            n +=1
            if n+1 == len(numbers):
                break
        answer[0] = numbers[len(numbers) - 1] 
    else:
        for num in numbers:
            answer[n-1] = num
            n +=1
    return answer