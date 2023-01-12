"""
4 rəqəmli tam müsbət ədəd verilmişdir.Bu ədədin öz rəqəmlərinin hamısına bölündüyünü təyin edin.
"""
eded = int(input("4 reqemli tam ededi daxil edin : "))

if (len(str(eded)) != 4):
    print("Eded 4reqemli deyil")
    exit()

reqemlerList = list(map(int, str(eded)))
if (eded % reqemlerList[0] == 0 and eded % reqemlerList[1] == 0 and eded % reqemlerList[2] == 0 and eded % reqemlerList[3] == 0):
    print("Beli , bolunur ")
else:
    print("Xeyr , bolunmur ")
