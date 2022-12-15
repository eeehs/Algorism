def solution(my_str, n):
    answer = []
    n_count = len(my_str)//n
    for i in range(n_count):
        answer.append(my_str[i*n:(i+1)*n])
    if len(my_str) % n !=0:
        answer.append(my_str[(i+1)*n:])

    return answer