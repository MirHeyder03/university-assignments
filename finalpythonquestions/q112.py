N = int(input("ededi daxil edin : "))
cem1 = 0
cem2 = 0
for i in range(1, N+1):
    cem1 += i**2
for i in range(1, N+1):
    cem2 += i**3

netice = (cem1/cem2)*100
print(netice)
