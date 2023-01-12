"""
Verilmiş sətirdə heç olmasa bir dənə   :   simvolu vardır. Birinci  :   işarəsindən sonra gələn simvollar ardıcıllığını ekrana çıxaran proqram tərtib etməli.
"""
string = input("string'i daxil edin : ")
metn = string.split(":")

for i in range(len(metn[1])):
    print(" Birinci :  işarəsindən sonra gələn simvollar : ",metn[1][i])
