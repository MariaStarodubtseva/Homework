my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(f'Исходный список: ', my_list)

ind = 0
new_gen_list = [el for ind, el in enumerate(my_list) if my_list[ind] > my_list[ind - 1]]
print(new_gen_list)

# или

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(f'Исходный список: ', my_list)
new_list = [el for el in my_list if el > my_list[my_list.index(el)-1]]
print(new_list)