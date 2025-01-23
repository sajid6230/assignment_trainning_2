#How do you find out if the two given strings are anagrams?


string1 = "triangle"
string2 = "integral"


count=0
for i in string1.lower():
    if i in string2.lower():
        count += 1
if len(string1) == len(string2):
    if count == len(string1):
        print("This is a anagram")
    else:
        print("Not anagram")
else:
    print("Not anagram")
