def solution(num_list, n):
    answer = []
    a = len(num_list) // n
    x = n
    m = 0
    while True:
        answer.append(num_list[m:n])
        m += x
        n += x 
        a -= 1 
        if a == 0:
            break
    return answer