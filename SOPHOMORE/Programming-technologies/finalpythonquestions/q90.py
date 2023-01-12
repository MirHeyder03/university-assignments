import random
list = [-1, -2, 1]

countplus = 0
countminus = 0
for i in list:
    if (i > 0):
        countplus += 1
    elif (i < 0):
        countminus += 1

def listDeyisme(list):
    if (countminus == countplus):
        return list
    elif (countplus > countminus):
        ferq1 = countplus-countminus
        for i in range(0, ferq1):
            list.append(random.randint(-10, 0))
    elif (countminus > countplus):
        ferq2 = countminus-countplus
        for j in range(0, ferq2):
            list.append(random.randint(0, 10))
    return list

print(listDeyisme(list))
