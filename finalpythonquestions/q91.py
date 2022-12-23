list = [-1, -2, -3, -3, -4, -5, 5, 4, 3, 2, 1]
list1 = []
list2 = []
for i in list:
    if (i > 0):
        list1.append(i**2)
    else:
        list2.append(i**3)
print("birinci siyahi : ", list1)
print("ikinci siyahi : ", list2)
