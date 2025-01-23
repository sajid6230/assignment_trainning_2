#How do you find the non-matching characters in a string?


string1 = "This is a cat"

string2 = "This is a Dog"

set1 = []
set2 = []

for i in string1.lower():
    if i not in string2.lower():
        set1.append(i)

for i in string2.lower():
    if i not in string1.lower():
        set2.append(i)

print("Present in string_1 but not in String_2 ",list(set(set1)))
print("Present in string_2 but not in String_1 ",list(set(set2)))