def solution(price):
    answer = 0
    if price >= 500000:
        price = price - (price * (20/100))
        answer = int(price)
    elif price >= 300000:
        price = price - (price * (10/100))
        answer = int(price)
    elif price >= 100000:
        price = price - (price * (5/100))
        answer = int(price)
    else:
        answer = price
    return answer
