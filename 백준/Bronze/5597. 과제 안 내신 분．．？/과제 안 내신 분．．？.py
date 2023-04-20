student = []
for i in range(1,31):
    student.append(i)
for i in range(28):
    A = int(input())
    student.remove(A)
for i in student:
    print(i)
