vowels = ['a', 'e', 'i', 'o', 'u']
x = input("Enter sentence: ")

count = 0

x = x.lower()

for i in x:
    if i in vowels:
        count += 1

print(count)