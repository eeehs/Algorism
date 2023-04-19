result = []
result_m = 0
while True:
    A = int(input())
    if A == 0:
        break
    else:
        result.append(A)
for m in result:
    for i in range(1,m+1):
        result_m += i
    print(result_m)
    result_m = 0
