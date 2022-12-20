

eded = int(input("tam eded daxil edin : "))
list = list(map(str, str(eded)))

list.append(list[0])
list.remove(list[0])
netice=int("".join(list))

print(netice)