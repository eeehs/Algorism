a,b = map(int, input().split())

n1 = a * (b/100)
result = a - n1
if result >= 100:
    print(0)
else:
    print(1)