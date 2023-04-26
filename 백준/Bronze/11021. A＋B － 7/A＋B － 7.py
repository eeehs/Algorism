T = int(input())
result = []
number = 1
for i in range(T):
    A , B = map(int, input().split())
    result.append(A+B)
for i in result:
    print(f"Case #{number}: {i}")
    number += 1