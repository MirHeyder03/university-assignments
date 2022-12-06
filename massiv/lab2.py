"""
B(n) ədədi massivinin elementlərinin hasilini hesablayan alqoritm tərtib etməli.
"""
n = int(input('Massivin ölçüsünü daxil edin : '))
B = []
for i in range(n):
    B.append(int(input("massivinin elementini daxil edin : ")))
hasil = 1
for i in range(len(B)):
    hasil *= B[i]

print("Massiv : ", B)
print("massivinin elementlərinin hasili : ", hasil)
