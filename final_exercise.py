my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
my_index = []
my_new_list = []
my_new_list_len = 0
number_to_found = 0
hits = 0

for i in range (len(my_list)):
    my_new_list.append(my_list[i])
    
for j in range (len(my_list)):
    number_to_found = my_list[j]

    for number in range (len(my_list)):
        if number_to_found in my_new_list:
            hits += 1
            if hits > 1:
                my_index.append(number)
            #my_new_list_len = len(my_new_list)
            #del my_new_list[my_new_list_len-1]
                hits = 1

        
#print("The list with unique elements only:")
print(my_list)
print(my_new_list)
print(my_index)
#print(my_hits)
