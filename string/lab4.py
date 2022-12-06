"""Verilmiş sətirdə iştirak edən bütün nida işarələrini  nöqtələrlə əvəz edən proqram tərtib etməli."""
string = input("string'i daxil edin : ")

if '!' in string:
    print(string.replace('!', '.'))
else:
    print('Cumlede ! isaresi yoxdur')