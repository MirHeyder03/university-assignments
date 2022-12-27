from math import *
N = int(input("ededi daxil edin : "))
list = list(str(N))

hendesiorta = 1
count = 0
for i in list:
    if int(i) % 2 == 0:
        hendesiorta *= sqrt(i)
        count += 1
print(hendesiorta)
