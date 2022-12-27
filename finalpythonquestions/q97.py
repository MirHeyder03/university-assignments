from random import *
list = []
for i in range(1, 3):
    list.append(randint(-10, 10))
cem = 0
count = 0
for i in list:
    cem += i
    if (i > 0):
        count += 1
list.insert(1, cem)
list.insert(2, count)
print(list)
