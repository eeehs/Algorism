def solution(slice, n):
    answer = 0
    total_slice = 0
    while True:
        if total_slice // n < 1:
            total_slice = total_slice + slice
        else:
            answer = total_slice // slice
            return(answer)
            break
