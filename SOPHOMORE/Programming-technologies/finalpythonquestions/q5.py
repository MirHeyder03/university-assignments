"""
Beş rəqəmli natural ədəd verilib.Ən solda yerləşən rəqəmdən başlayaraq bütün rəqəmlərin bütün rəqəmlərin artma sırası ilə yerləşdiyini müəyyən etmək lazımdır.
"""
eded = int(input("5 reqemli eded daxil edin : "))
reqem1 = eded // 10000
reqem2 = (eded // 1000) % 10
reqem3 = (eded // 100) % 10
reqem4 = (eded // 10) % 10
reqem5 = eded % 10
if reqem1 < reqem2 and reqem2 < reqem3 and reqem3 < reqem4 and reqem4 < reqem5:
    print('Rəqəmlər artan sırada düzülüb')
else:
    print('Rəqəmlər artan sırada düzülməyib')