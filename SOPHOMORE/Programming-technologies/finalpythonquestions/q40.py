cem1 = 0
cem2 = 0
for i in range(1, 100):
    if (i % 3 == 0):
        cem1 += i
    elif (i % 3 != 0):
        cem2 += i

netice = (cem1/cem2)*100
print(netice)
