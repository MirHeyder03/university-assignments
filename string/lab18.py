"""
Verilmiş sətirdə hər bir chaild hərflər qrupunu children hərflər qrupu ilə əvəz edən proqram tərtib etməli. 
"""
string = input("string'i daxil edin : ")
if 'chaild' in string:
    print(string.replace("chaild", "children"))
else:
    print('Cumlede  chaild hərflər qrupu yoxdur')
