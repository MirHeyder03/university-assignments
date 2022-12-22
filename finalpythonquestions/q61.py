N = int(input("ededi daxil edin : "))
listN = list(str(N))
list = []

for i in listN:
    if (listN.count(i) == 2):
        list.append(i)
print("iki defe tekrarlanan reqemler  : ", set(list)) #set - tekrarin qarsini almaq ucun
