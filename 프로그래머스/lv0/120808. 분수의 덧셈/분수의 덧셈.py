def solution(denum1, num1, denum2, num2):
    i = 0
    answer = []
    denum = denum1 * num2 + denum2 * num1
    num = num1 * num2

    for nu in range(1,num + 1):
        if num % nu == 0 and denum % nu == 0:
            if nu > i:
                i = nu
    answer.append(int(denum / i))
    answer.append(int(num / i))
    return answer