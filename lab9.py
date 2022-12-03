"""
C(n) ədədi massivinin cüt indeksli elementlərinin cəmini hesablayan alqoritm tərtib etməli.
"""
n = int(input('Massivin ölçüsünü daxil edin : '))
C = []
for i in range(n):
    C.append(int(input("massivinin elementini daxil edin : ")))

cem = 0
for i in range(len(C)):
    if (i % 2 == 0):
        cem += C[i]

print("Massiv : ", C)
print("cüt indeksli elementlərinin cəmini : ", cem)
