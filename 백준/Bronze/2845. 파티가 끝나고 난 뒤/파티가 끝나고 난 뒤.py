P , M = map(int,input().split())
WL = list(map(int,input().split()))

total = P * M
total_list = []
for i in WL:
    result = i - total
    print(result, end=" ")