N = int(input("ededi daxil edin : "))
listN = list(str(N))
list = []

for i in listN:
    if (listN.count(i) == 1):
        list.append(i)
print("bir defe tekrarlanan reqemler  : ", list)
