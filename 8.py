#How do you total all of the matching integer elements in an array?

list_1 = [1,2,3,4,2,3,4,5,6,7,1,2,4,5,6,3]

dict = {}
for i in list_1:
    if list_1.count(i) > 1:
        if i in dict:
            dict[i] += i
        else:
            dict[i] = i  

print(dict)

for key, value in dict.items():
    print(f"Total for {key}: {value}")
    