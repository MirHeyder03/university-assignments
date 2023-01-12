"""
Üç rəqəmli natural ədəd verilib.Onun Armstronq ədədi olub olmadığını müəyyən edin.
"""
eded = int(input("Ədədi daxil edin : "))
cem = 0
temp = eded
while temp > 0:
    reqem = temp % 10
    cem += reqem**3
    temp //= 10

if eded == cem:
    print(eded, " Armstronq ədədidir")
else:
    print(eded, " Armstronq ədədi deyil")
