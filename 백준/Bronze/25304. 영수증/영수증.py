X = int(input()) # 총금액
N = int(input()) # 물건 갯수
result = 0
for i in range(N):
    a,b = map(int, input().split())
    result += a*b
if X == result:
    print("Yes")
else:
    print("No")