"""
Verilmiş sətirdə sol və sağ mötərizələr arasında qalan bütün simvolları mötərizələrlə birlikdə aradan çıxaran proqram tərtib etməli. 
"""
string = input('Setr daxil edin: ')

index1 = string.index("(")
index2 = string.index(")")
araliq = string[index1:index2+1]
string = string.replace(araliq, "")

print(string)
