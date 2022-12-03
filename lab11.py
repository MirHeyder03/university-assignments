"""
B(n) ədədi massivinin tək indeksli elementlərinin cəmini hesablayan alqoritm tərtib etməli.
"""
n = int(input('Massivin ölçüsünü daxil edin : '))
B = []
for i in range(n):
    B.append(int(input("massivinin elementini daxil edin : ")))

cem = 0
for i in range(len(B)):
    if (i % 2 != 0):
        cem += B[i]

print("Massiv : ", B)
print("tək indeksli elementlərinin cəmini : ", cem)
