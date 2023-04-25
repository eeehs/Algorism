N = int(input())
result = [input() for i in range(N)]
for i in result:
    print(i[0]+i[len(i)-1])