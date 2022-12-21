from math import *
a = int(input("a-ni daxil edin : "))
b = int(input("b-ni daxil edin : "))
c = int(input("c-nidaxil edin : "))

p = (a+b+c)/2  #!yarim perimeter
S = sqrt(p*(p-a)*(p-b)*(p-c)) #!sahesi

print(S)