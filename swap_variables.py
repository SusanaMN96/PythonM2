variable_1 = 1
variable_2 = 2

variable_1, variable_2 = variable_2, variable_1

print(variable_2, variable_1)

my_list = [10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)

my_list = [10, 1, 8, 3, 5, 9,0]
length = len(my_list)

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)
