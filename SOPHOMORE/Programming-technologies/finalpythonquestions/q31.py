eded = int(input("tam eded daxil edin : "))
list = list(map(str, str(eded)))

yuzluk = eded//100 % 10
onluq = eded//10 % 10
print(list)
temp = list[list.index(str(yuzluk))]
list[list.index(str(yuzluk))] = list[list.index(str(onluq))]
list[list.index(str(onluq))]=temp


print(list)

netice=int("".join(list))
print(netice)
