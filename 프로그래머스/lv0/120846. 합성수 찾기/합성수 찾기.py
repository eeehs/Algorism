def solution(n):
    answer = 0
    count = 0
    for i in range(4, n+1):
        for m in range(1, 101):
            if i >= m and i % m == 0:
                count += 1
        if count >= 3:
            count = 0
            answer += 1    
    return answer