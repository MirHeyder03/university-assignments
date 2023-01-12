eded = int(input("ededi daxil edin : "))

ededList = list(str(eded))

cem1 = 0
for i in range(len(ededList)):
    cem1 += int(ededList[i])**3

cem2 = 0
for i in range(len(ededList)):
    cem2 += int(ededList[i])**2

tam = cem1//cem2
qaliq = cem1-(tam*cem2)
print("reqemlerin kublari cemi : ", cem1)
print("reqemlerin kvadratlari cemi : ", cem2)
print("tam : ", tam)
print("qaliq : ", qaliq)
