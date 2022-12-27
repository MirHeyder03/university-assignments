N = int(input("ededi daxil edin : "))
list = list(str(N))

cem = 0
count=0
for i in list:
    if int(i) % 2 != 0:
        count+=1
        cem += int(i)
ededorta=cem/count
print(ededorta)