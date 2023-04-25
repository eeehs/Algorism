N = int(input())
result = []
for i in range(N):
    M = list(map(int, input().split()))
    result.append(M)
for i in result:
    print(sum(i))