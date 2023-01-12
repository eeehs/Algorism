def solution(sides):
    answer = 0
    sides = sorted(sides)
    # sides[1]가 가장 긴 변일 경우
        # sides[1] < sides[0] + ? and ? <= sides[1]
    for i in range((sides[1]-sides[0]+1),(sides[1]+1)):
        answer +=1
    # 다른 변이 가장 긴 변일 경우 
        # ? < sides[1] + sides[0] and sides[1] <= ?
    for i in range(sides[1]+1, sides[1] + sides[0]):
        answer +=1
    return answer