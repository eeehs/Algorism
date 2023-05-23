moun = ['a','e','i','o','u','A','E','I','O','U']
result = []
counter = 0
while True:
    A = input()
    if A == "#":
        break
    for i in moun:
        counter +=A.count(i)
    result.append(counter)
    counter = 0
for i in result:
    print(i)