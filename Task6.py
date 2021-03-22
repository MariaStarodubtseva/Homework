from itertools import count

for el in count(3):
    if el > 10:
        break
    print(el)

from itertools import cycle

my_list = [True, 'ABC', 123, None]
c = 0
for el in cycle(my_list):
    if c > 10:
        break
    print(el)
    c += 1