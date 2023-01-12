"""
Verilmiş sətirdə iştirak edən hər bir nöqtəni üç nöqtə ilə əvəz edən proqram tərtib etməli.
"""
string = input("string'i daxil edin : ")

if '.' in string:
    print(string.replace('.', '...'))
else:
    print('Cumlede . isaresi yoxdur')