"""
Verilmiş sətirdə heç olmasa bir dənə vergül işarəsi vardır. Sətirdə iştirak edən birinci vergül işarəsinin sıra nömrəsini təyin edən proqram tərtib etməli.
"""
string = input("string'i daxil edin : ")

if ',' in string:
    print(string.index(','))
else:
    print('Cumlede , isaresi yoxdur')