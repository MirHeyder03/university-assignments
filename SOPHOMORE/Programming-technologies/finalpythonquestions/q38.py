beseBolunen = 0
beseBolunmeyen = 0
for i in range(1, 100):
    if (i % 5 == 0):
        beseBolunen += i
    elif (i % 5 != 0):
        beseBolunmeyen += i
netice=beseBolunen-beseBolunmeyen
print(netice)