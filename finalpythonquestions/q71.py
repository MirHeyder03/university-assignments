n = int(input("ayin nomresini daxil edin : "))


def hesabla(n):
    if (n <= 0 or n > 31):
        return "zehmet olmasa duz daxil edin"
    if (n == 2):
        return "ya 28 gundur yada 29"
    elif (n == 4 or n == 6 or n == 9 or n == 11):
        return 30
    else:
        return 31


print(hesabla(n))
