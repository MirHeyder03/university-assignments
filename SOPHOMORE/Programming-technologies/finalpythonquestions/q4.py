"""
4 rəqəmli natural ədəd verilmişdir.Onun palindrom ədəd olduğunu müəyyən edin
"""
eded = int(input("4 reqemli eded daxil edin : "))


def palindrom(eded):
    rev = 0
    i = eded
    while i > 0:
        rev = rev * 10 + i % 10
        i //= 10
    return (eded == rev)

if (palindrom(eded)):
    print("Eded palindromdur")
else:
    print("Eded palindrom deyil")
