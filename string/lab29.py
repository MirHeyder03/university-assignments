"""
Azərbaycan dilində sətir cümlə verilmişdir. Sətiri elə çevirməli ki, bütün sözlər böyük hərflərlə başlasın.
"""
string=input("Cumleni daxil edin : ")
list=string.split()
for i in range(len(list)):
    list[i]=list[i].capitalize()

string=" ".join(list)
print(string)