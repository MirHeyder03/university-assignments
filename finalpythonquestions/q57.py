eded = int(input("ededi daxil edin : "))

ededList = list(str(eded))

cem = 0
for i in range(len(ededList)):
    cem += int(ededList[i])**3

print(cem)
