rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('task4.txt', 'r') as f:
    #content = file_obj.read().split('\n')
    for i in f:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)
with open('task4_new.txt', "w") as f_2:
    f_2.writelines(new_file)
