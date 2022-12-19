a = int(input("1-ci ededi daxil edin : "))
b = int(input("2-ci ededi daxil edin : "))
c = int(input("3-ci ededi daxil edin : "))


def hellEt(a, b, c):
    if (a == b and b == c and c == a):
        return 3
    elif (a == b or b == c or c == a):
        return -2
    else:
        return 0


print(hellEt(a, b, c))
