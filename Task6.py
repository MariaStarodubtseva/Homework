with open("task6.txt", "r") as f:
    my_list = f.readlines()

answer = {}
for ii in my_list:
    subject, hours = ii.split(':')
    abc = []
    for h in hours.split():
        hour = ''.join(filter(lambda x: x.isdigit(), h))
        if hour.isdigit():
            abc.append(int(hour))
    answer[subject] = sum(abc)
print(answer)