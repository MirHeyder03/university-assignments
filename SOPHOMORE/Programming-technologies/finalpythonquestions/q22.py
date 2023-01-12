N = int(input("ededi daxil edin : "))
Nlist = list(map(int, str(N)))
yeniList = []
for i in range(len(Nlist)):
    if (Nlist[i] % 2 != 0):
        yeniList.append(Nlist[i])
N = "".join(map(str, yeniList))
print(N)
