"""
Dörd rəqəmli natural ədəd verilib.Onun rəqəmlərinin bir birindən fərqli olduğunu müəyyən edin.Əgər fərqlidisə , Yes çıxışı edin,əks halda No.
"""
eded = int(input("4 reqemli tam ededi daxil edin : "))
reqem1 = eded//1000
reqem2 = eded//100 % 10
reqem3 = eded//10 % 10
reqem4 = eded % 10


if ((reqem1 != reqem2) and (reqem2 != reqem3) and (reqem3 != reqem4) and (reqem4 != reqem1)):
    print("Beli , ferqlidir ")
else:
    print("Xeyr , ferqli deyil ")
