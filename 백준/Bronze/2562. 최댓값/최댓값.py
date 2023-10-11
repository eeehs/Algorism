a = 0 # 최댓값 순서
A = 0 # 최댓값

for i in range(9):
    q = int(input())
    if q > A:
        A = q
        a = i + 1
print(A)
print(a)