"""
B(n) ədədi massivinin 9-dan böyük elementlərinin hasilini hesablayan alqoritm tərtib etməli.
"""
n = int(input('Massivin ölçüsünü daxil edin : '))
B = []
for i in range(n):
    B.append(int(input("massivinin elementini daxil edin : ")))

hasil = 1
for i in range(len(B)):
    if (B[i] > 9):
        hasil *= B[i]

print("Massiv : ", B)
print("9-dan böyük elementlərinin hasili : ", hasil)
