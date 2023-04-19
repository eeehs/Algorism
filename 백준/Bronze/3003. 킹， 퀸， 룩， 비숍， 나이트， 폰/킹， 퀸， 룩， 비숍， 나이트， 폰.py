chess = [1,1,2,2,2,8]
N = list(map(int, input().split()))
output = []
for i in range(len(chess)):
    result = str(chess[i] - N[i])
    output.append(result)
print(" ".join(output))
