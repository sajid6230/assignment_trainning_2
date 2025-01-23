#How do you find the maximum element in an array?

list_1 = [21,2334,65457,58,67962,342,4564,23423,567]


list_1.sort()
len_list = len(list_1)

print("Maximum element of list_1 is : ", list_1[len_list-1])


#alternatively we can use max() function