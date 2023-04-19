result = []
while True:
    try:
        A,B = map(int, input().split())
        result.append(B//(A+1))
    except:
        break
for i in result:
    print(i)