netice=[]
for i in range(10000, 100000):
    listI = list(str(i))
    cem = 0
    hasil = 1
    for j in listI:
        cem += int(j)
    for k in listI:
        hasil *= int(k)
    if(cem == hasil):
        netice.append(i)

print("cem = ", cem)
print("hasil = ", hasil)
print("netice = ", netice)
