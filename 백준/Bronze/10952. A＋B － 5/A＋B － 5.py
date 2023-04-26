result = []
while True:
    A, B = map(int, input().split())
    if A + B == 0:
        break
    else:
        result.append(A+B)
for i in result:
    print(i)