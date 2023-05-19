count = 1
result = []
while True:
    N = list(map(int, input().split()))
    if N[0] == 0:
        break
    else:
        result.append(f"Case {count}: Sorting... done!")
        count +=1
for i in result:
    print(i)