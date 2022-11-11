def solution(num_list):
    answer = []
    a = 0 
    b = 0
    for i in num_list:
        if i % 2 == 1:
            a = a + 1 
        else:
            b = b + 1
    answer.append(b)
    answer.append(a)
    return answer