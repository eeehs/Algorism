N,A,B = map(int, input().split())

if N > A:
    print("Bus")
elif N == A:
    if A == B:
        print("Anything")
    else:
        print("Bus")
else:
    if A > B:
        print("Subway")
    elif A == B:
        print("Anything")
    else:
        print("Bus")
