"""
C(n) ədədi massivinin tək indeksli elementlərinin hasilini hesablayan alqoritm tərtib etməli
"""
n = int(input('Massivin ölçüsünü daxil edin : '))
C = []
for i in range(n):
    C.append(int(input("massivinin elementini daxil edin : ")))

hasil = 1
for i in range(len(C)):
    if (i % 2 != 0):
        hasil *= C[i]

print("Massiv : ", C)
print("tək indeksli elementlərinin hasili : ", hasil)
