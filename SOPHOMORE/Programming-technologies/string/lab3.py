"""
Verilmiş sətirdə    +,  -  , *  simvollarının ümumi sayını hesablayan proqram tərtib etməli.
"""
string = input("string'i daxil edin : ")
countPlus = string.count("+")
countMinus = string.count("-")
countMultiplication = string.count("*")
result = countPlus+countMinus+countMultiplication
print(result)