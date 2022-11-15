def solution(balls, share):
    answer = 0
    total_balls = 1
    shares = 1
    balls_shares = 1
    for i in range(1,balls+1):
        total_balls *= i
    for n in range(1,share+1):
        shares *=n
    for m in range(1,balls-share+1):
        balls_shares *=m
        
    answer = (total_balls) // (balls_shares * shares)
    return answer