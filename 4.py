# How do you find the count for the occurrence of a particular character in a string?

a = ("This is a sentence")
a1 = a.lower()

while True:
    b = input("Enter a letter: ").lower()
    if (b.isalpha() or b.isdigit()) and len(b) ==1:
        break
    else:
        print("Invalid input. Please enter a single alphabet or digit.")


count = 0
for i in a1:
    if i == b:
        count += 1 

print(f"The count of '{b}' in the string is : {count}")