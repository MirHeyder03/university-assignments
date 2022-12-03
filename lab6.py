"""
C(n) ədədi massivinin mənfi elementlərinin hasilini hesablayan alqoritm tərtib etməli
"""
n = int(input('Massivin ölçüsünü daxil edin : '))
C = []
for i in range(n):
    C.append(int(input("massivinin elementini daxil edin : ")))

hasil = 1
for i in range(len(C)):
    if (C[i] < 0):
        hasil *= C[i]

print("Massiv : ", C)
print("mənfi elementlərinin hasili : ", hasil)
