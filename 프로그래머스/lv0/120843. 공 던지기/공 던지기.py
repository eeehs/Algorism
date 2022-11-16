def solution(numbers, k):
    routine = []
    n = 1
    while True:
        for i in numbers:
            routine.append(i)
        if (k * 2) < len(routine):
            break
    for ro in range(1,len(routine),2):
        if n == k:
            answer = routine[ro-1]
        n +=1
    return answer
        
        
