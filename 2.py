#How do you determine if a string is a palindrome?

a = input("Enter a word: ")

a1 = a.replace(" ","").lower()

b = a1[::-1]


if b == a1 :
    print("Palindrome")
else:
    print("Not Palindrome")