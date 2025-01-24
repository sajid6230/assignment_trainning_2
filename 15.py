#How do you check if an integer is even or odd?

def even_odd(num):

    if num % 2 == 0:
        return "The number is Even "
    else:
        return "The number is Odd "
    


result = even_odd(50)
print(result)