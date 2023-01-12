"""
B(n) ədədi massivinin  tək indeksli elementlərinin ədədi ortasını hesablayan alqoritm tərtib etməli
"""
n = int(input('Massivin ölçüsünü daxil edin : '))
B = []
for i in range(n):
    B.append(int(input("massivinin elementini daxil edin : ")))

cem = 0
tekIndexSayi = 0
for i in range(len(B)):
    if (i % 2 != 0):
        cem += B[i]
        tekIndexSayi += 1

edediOrta = cem/tekIndexSayi
print("tək indeksli elementlərinin ədədi ortasi : ", edediOrta)
