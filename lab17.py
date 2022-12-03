"""
C(n) ədədi massivinin  tək indeksli elementlərinin hesabi ortasını hesablayan alqoritm tərtib etməli.
"""
n = int(input('Massivin ölçüsünü daxil edin : '))
C = []
for i in range(n):
    C.append(int(input("massivinin elementini daxil edin : ")))

cem = 0
tekIndexSayi = 0
for i in range(len(C)):
    if (i % 2 != 0):
        cem += C[i]
        tekIndexSayi += 1

print("tək indeksli elementlərinin ədədi ortasi : ")
