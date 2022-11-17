def solution(numbers):
    answer = 0
    a = sorted(numbers)
    answer = a[len(a)-1] * a[len(a)-2]
    return answer