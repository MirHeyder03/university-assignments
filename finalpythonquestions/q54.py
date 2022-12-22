eded = int(input("ededi daxil edin : "))

ededList = list(str(eded))
hasil = 1
for i in range(len(ededList)):
    hasil *= int(ededList[i])

print(hasil)
