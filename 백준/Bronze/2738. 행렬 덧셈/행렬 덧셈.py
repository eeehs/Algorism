N,M = map(int, input().split())

result_A = []
result_B = []
results = []
for i in range(N):
    input_A = list(map(int, input().split()))
    result_A.append(input_A)

for i in range(N):
    input_B = list(map(int, input().split()))
    result_B.append(input_B)

for i in range(N):
    for m in range(M):
        result = result_A[i][m] + result_B[i][m]
        results.append(str(result))
    print(" ".join(results))
    results = []