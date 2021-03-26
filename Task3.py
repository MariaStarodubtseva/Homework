with open('task3.txt', 'r') as f:
    sal = []
    poor = []
    my_list = f.read().strip().split('\n')
    for i in my_list:
        i = i.split()
        salary = int(i[1 ])
        if salary >= 20000:
            pass
        else:
            poor.append(i[0])
        sal.append(i[1])
print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(int, sal)) / len(sal)}')
