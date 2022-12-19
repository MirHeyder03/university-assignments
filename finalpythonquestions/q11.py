N=int(input("ededi daxil edin : "))

NList=list(map(int,str(N)))

cem=0
hasil=1
for i in range(len(NList)):
    hasil*=NList[i]
    cem+=NList[i]
print("reqemlerinin cemi: ", cem)
print("reqemlerinin hasili: ", hasil)
