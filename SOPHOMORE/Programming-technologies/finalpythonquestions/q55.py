eded = int(input("ededi daxil edin : "))

ededList = list(str(eded))
hasil = 1
for i in range(len(ededList)):
    hasil *= int(ededList[i])

cem = 0
for i in range(len(ededList)):
    cem += int(ededList[i])

netice = int(hasil/cem)  # tam hisseni istediyi ucun
print(netice)
