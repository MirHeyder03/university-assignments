from random import *
list = []
for i in range(1, 5):
    list.append(randint(-10, 10))
cem = 0
count = 0
mid = len(list) // 2
left = list[0:mid]
right = list[mid:]

temp = right
left = temp
right = left



print(list)
