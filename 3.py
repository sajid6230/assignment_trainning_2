#How do you calculate the number of numerical digits in a string?


a = ("Hellow12 World123! ")

digits = []
for i in a:
    if i.isdigit():
        digits.append(int(i))

print(sum(digits))
