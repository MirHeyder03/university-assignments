"""
Verilmiş sətirdə ardıcıl olaraq gələn iki dənə A simvolunun yerləşdiyi simvollar qrupunnun sıra nömrəsini təyin edən proqram tərtib etməli.
"""
string = input("string'i daxil edin : ")

if 'AA' in string:
    print(string.index('A'))
else:
    print('Cumlede ardicil A isaresi yoxdur')