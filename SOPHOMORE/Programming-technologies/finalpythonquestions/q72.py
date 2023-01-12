n = int(input("ayin nomresini daxil edin : "))
m = int(input("gunun nomresini daxil edin : "))

def hesabla(n, m):
    if (n <= 0 or m <= 0 or m > 31 or n > 12):
        return "zehmet olmasa duzgun daxil edin"
    if (n == 3 and m >= 21) or (n == 4 and 1 < m < 31) or (n == 5 and 1 < m <= 31) or (n == 6 and 1 < m < 22):
        return "Yaz"
    elif (n == 6 and m >= 22) or (n == 7 and 1 < m <= 31) or (n == 8 and 1 < m <= 31) or (n == 9 and 1 < m < 23):
        return "Yay"
    elif (n == 9 and m >= 23) or (n == 10 and 1 < m < 31) or (n == 11 and 1 < m < 31) or (n == 12 and 1 < m < 22):
        return "Payiz"
    elif (n == 12 and m >= 22) or (n == 1 and 1 < m <= 31) or (n == 2 and 1 < m <= 29 ) or (n == 3 and 1 < m < 21):
        return "Qis"

print(hesabla(n, m))
