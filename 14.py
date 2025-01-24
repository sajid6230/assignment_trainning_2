#How do you find the average of numbers in a list?



def avg_list(list):
    
    sum1 = sum(list)
    avg = sum1 / len(list)
    return(avg)

avg1 = avg_list([2,3,4,5])
print("Average of the list if: ",avg1)
