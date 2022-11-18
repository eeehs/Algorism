def solution(n):
    answer = 0
    packs = 1
    
    while True:
        a = 1
        for pack in range(1,packs+1):
            a *= pack
        if a == n:
            answer = packs
            break
        elif a > n:
            answer = packs - 1
            break
        else:
            packs += 1
    return answer