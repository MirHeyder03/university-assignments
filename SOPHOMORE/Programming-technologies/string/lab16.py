"""
Verilmiş sətrə abs hərflər qrupunun neçə dəfə daxil olduğunu təyin edən proqram tərtib etməli.
"""
string = input("string'i daxil edin : ")
if 'abs' in string:
    print(string.count("abs"))
else:
    print('Cumlede  abs hərflər qrupu yoxdur')
