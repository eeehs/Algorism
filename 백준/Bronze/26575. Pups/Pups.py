N = int(input())
result = []
for i in range(N):
    d,f,p = map(float, input().split())
    dfp = format(d*f*p,".2f")
    result.append(dfp)
for i in result:
    print(f"${i}")
