"""
A(n) ədədi massivinin cüt indeksli elementlərinin hasilini hesablayan alqoritm tərtib etməli
"""
n = int(input('Massivin ölçüsünü daxil edin : '))
A = []
for i in range(n):
    A.append(int(input("massivinin elementini daxil edin : ")))

hasil = 1
for i in range(len(A)):
    if (i % 2 == 0):
        hasil *= A[i]

print("Massiv : ", A)
print("cüt indeksli elementlərinin hasili : ", hasil)
