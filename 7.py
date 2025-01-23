#How do you calculate the number of vowels and consonants in a string?

a1 = "aeiou bcdf 21342"
a = a1.replace(" ","").lower()
count_v = 0
count_c = 0
vowel = ("a","e","i","o","u")

for i in a:
    if i in vowel:
        count_v += 1
    elif i.isalpha():
        count_c += 1

print("Number of Vowel : ", count_v)
print("Number of Consonant : ", count_c)