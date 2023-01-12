"""
Verilmiş sətirdə ardıcıl olaraq gələn probel(boşluq) simvollarının sayının ən böyük qiymətini təyin edən proqram tərtib etməli.
"""
string = input("string'i daxil edin : ")

if '  ' in string:
    print(string.count("  "))
else:
    print('Cumlede ardicil bosluq ardicil yoxdur')
