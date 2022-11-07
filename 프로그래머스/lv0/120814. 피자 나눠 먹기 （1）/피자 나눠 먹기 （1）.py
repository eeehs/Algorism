def solution(n):
    answer = 0
    pizza = 1
    
    pizza_divide = (pizza * 7) / n
    while True:
        if pizza * 7 < n:
            pizza += 1
        else:
            answer = pizza
            return answer
            break
    