for i in range(0,5):
    print("#")
    print (i)

var = 1
while var > 10:
    print("#")
    var = var << 20
    print(var)

my_list = [1, 2, 3]
for v in range(len(my_list)):
    my_list.insert(1, my_list[v])
    print(v)
print(my_list)

i = 1
while i <= 3:
    i+=2
    print("*")
    print(i)

a = 1
b = 1
c= a^b
print(c)
