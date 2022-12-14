"""
Verilmiş sətirə  * simvolu daxil deyilsə, sətri dəyişməməli, əks halda *  simvolundan sonra gələn hər bir birinci simvolu  - (tire)  simvolu ilə əvəz edən proqram tərtib etməli.
"""



# def replaceCharacter (string): 
#     newString = "" 
#     foundAsterisk = False
#     for i in range (len (string)): 
#         if string [i] == ' * ': 
#             foundAsterisk = True
#             newString += ' * '
#         elif foundAsterisk == True: 
#             newString += ' - ' 
#             foundAsterisk = False 
#         else: 
#             newString += string [i] 
#     return newString 

# print (replaceCharacter ('Test*String')) 
# print (replaceCharacter ('TestString'))
# replaceCharacter ('Test*String')




# string = input("Input a string containing the * character: ")

# if "*" not in string:
#     print(string)
# else:
#     result = ""
#     for i in range(len(string)):
#         if string[i] == "*":
#             result += "*" + "-"
#         else:
#             result += string[i]

# print(result)



dizi = "HackerLand*University"

def karakter_degistir (dizi): 
  sonuc = "" 
  for harf in dizi: 
    if harf == '*': 
      sonuc += '-' 
    elif harf != '*':
      sonuc += harf
  return sonuc

print(karakter_degistir(dizi))