N = int(input("ededi daxil edin : "))

list = list(str(N))
def hesabla(list):
    count = 0
    reqem = list[0]
    for i in list:
        tekrar = list.count(i)
        if (tekrar > count):
            count = tekrar
            eded = i
    return eded

print(hesabla(list))
