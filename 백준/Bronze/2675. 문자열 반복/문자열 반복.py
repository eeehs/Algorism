result = ""
result_list = []


T = int(input())
for i in range(T):
    R,S = input().split()
    for s in S:
        result +=  s * int(R)
    result_list.append(result)
    result = ""
for i in range(T):
    print(result_list[i])
