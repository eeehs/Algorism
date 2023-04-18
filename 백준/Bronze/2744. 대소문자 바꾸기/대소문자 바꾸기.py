n = input()
word = ""
for i in n:
    if i.isupper():
        word += i.lower()
    else:
         word += i.upper()
print(word)