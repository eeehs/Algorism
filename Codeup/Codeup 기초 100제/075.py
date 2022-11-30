# 정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.

n = int(input())
order = n - n 
while True:
    print(order)
    order +=1
    if order == n+1:
        break