
eded=int(input("ededi daxil edin : "))
list=[]
for i in range(1,eded):
    if(eded % i == 0):
        list.append(i)
cem=0
for i in range(len(list)):
    cem+=list[i]

if(eded==cem):
    print("Eded mukemmeldir")
else:
    print("Eded mukemmel deyil")