"""
Verilmiş sətirdə ardıcıl olaraq gələn abcd hərflər qrupunu silən  proqram tərtib etməli.
"""
string = input("string'i daxil edin : ")
if 'abcd' in string:
    print(string.replace('abcd',"") )
else:
    print('Cumlede abcd ardicil herfleri yoxdur')