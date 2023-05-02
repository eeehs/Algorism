N = int(input())
result = []
for i in range(N):
    A,B,C,D = map(int, input().split())
    if (A*B) > (C*D):
        result.append("TelecomParisTech") 
    elif (A*B) == (C*D):
        result.append("Tie") 
    else:
        result.append("Eurecom")
for i in result:
    print(i)