"""
Verilmiş sətirdə iştirak edən bütün  *  simvollarını aradan çıxarmalı və ulduzdan fərqli hər bir simvolu təkrar edərək yeni sətri ekrana çıxaran  proqram tərtib etməli.
"""
string = input("string'i daxil edin : ")
if '*' in string:
    print(string.replace('*',"-") )
else:
    print('Cumlede * isaresi yoxdur')