"""
Verilmiş sətrə aba hərflər qrupunun neçə dəfə daxil olduğunu təyin edən proqram tərtib etməli.
"""
string = input("string'i daxil edin : ")
if 'aba' in string:
    print(string.count("aba"))
else:
    print('Cumlede  aba hərflər qrupu yoxdur')