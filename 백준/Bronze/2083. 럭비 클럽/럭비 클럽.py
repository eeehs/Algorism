member = []
while True:
    Name , age , kiro = input().split()
    if Name == "#":
        break
    else:
        if int(age) > 17 or int(kiro) >= 80:
            member.append(f"{Name} Senior")
        else:
            member.append(f"{Name} Junior")
for i in member:
    print(i)