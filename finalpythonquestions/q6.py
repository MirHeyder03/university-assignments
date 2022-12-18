"""
4 rəqəmli tam müsbət ədəd verilmişdir.Bu ədədin öz rəqəmlərinin hamısına bölündüyünü təyin edin.
"""
eded = int(input("4 reqemli tam ededi daxil edin : "))

reqem1 = eded // 1000
reqem2 = (eded // 100) % 10
reqem3 = (eded // 10) % 10
reqem4 = eded % 10

if (eded % reqem1 == 0 and eded % reqem2 == 0 and eded % reqem3 == 0 and eded % reqem4 == 0):
    print("Beli , bolunur ")
else:
    print("Xeyr , bolunmur ")
