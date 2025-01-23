#How do you reverse an array?


list_1 = [1,2,3,4,5,6,7,8,9,"A","B","C"]

reverse_list = []

for i in range(len(list_1)-1,-1, -1):
    reverse_list.append(list_1[i])
    
print("Given array : ", list_1)
print("Reverse array : ", reverse_list)