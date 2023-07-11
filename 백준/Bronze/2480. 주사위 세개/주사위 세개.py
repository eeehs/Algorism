jusawi = list(map(int,input().split()))
jusawi = sorted(jusawi)

times = 1
number = 0 
for i in jusawi:
    if jusawi.count(i) > times:
        times = jusawi.count(i)
        number = i

if times == 3:
    print(10000 + (number * 1000))
elif times == 2:
    print(1000+(number * 100))
else:
    print(jusawi[-1]*100)