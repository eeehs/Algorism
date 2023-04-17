G = map(int,input().split())
result = 0
for i in G:
    result += i * i
result = result % 10
print(result)  
