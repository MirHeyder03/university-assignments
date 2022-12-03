"""
C(n) ədədi massivinin  3-ə böldükdə qalıqda iki alınan elementlərinin   ədədi  ortasını hesablayan alqoritm tərtib etməli.
"""
n = int(input('Massivin ölçüsünü daxil edin : '))
C = []
for i in range(n):
    C.append(int(input("massivinin elementini daxil edin : ")))

cem = 0
count = 0
for i in range(len(C)):
    if (C[i] % 3 == 2):
        cem += C[i]
        count += 1

if (count == 0):
    print("3-ə böldükdə qalıqda iki alınan eded yoxdur")
else:
    edediOrta = cem/count
    print("3-ə böldükdə qalıqda iki alınan elementlərinin   ədədi  ortası : ", edediOrta)
