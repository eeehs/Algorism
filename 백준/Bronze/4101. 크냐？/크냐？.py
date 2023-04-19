result = []
while True:
    A = list(map(int, input().split()))
    if (A[0]== 0 and A[1] == 0):
        break 
    else:
        if A[0] > A[1]:
            result.append("Yes")
        else:
            result.append("No")
for i in result:
    print(i)