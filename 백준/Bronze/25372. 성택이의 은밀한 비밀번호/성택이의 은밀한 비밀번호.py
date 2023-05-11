N = int(input())
result = []
for i in range(N):
    password = input()
    if (6 <= len(password)) and (9 >= len(password)):
        result.append("yes")
    else:
        result.append("no")
for i in result:
    print(i)