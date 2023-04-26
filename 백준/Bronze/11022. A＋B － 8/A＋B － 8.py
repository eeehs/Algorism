T = int(input())
result = []
number = 1
for i in range(T):
    A , B = map(int, input().split())
    sum_A_B = f"Case #{i+1}: {A} + {B} = {A+B}"
    result.append(sum_A_B)
for i in result:
    print(i)

