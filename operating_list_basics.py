my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
to_find = 10
found = False
hint = 0
my_index = []
my_new_list = []

for i in range (len(my_list)):
    
    if my_list[i] in my_new_list:
        continue
    if my_list[i] not in my_new_list:
        my_new_list.append(my_list[i])

my_list = my_new_list
    
print(my_list)
print(set(my_list))
print(my_new_list)
