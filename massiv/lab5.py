"""
B(n) ədədi massivinin mənfi elementlərinin cəmini hesablayan alqoritm tərtib etməli
"""
n = int(input('Massivin ölçüsünü daxil edin : '))
B = []
for i in range(n):
    B.append(int(input("massivinin elementini daxil edin : ")))

cem = 0
for i in range(len(B)):
    if (B[i] < 0):
        cem += B[i]

print("Massiv : ", B)
print("Mənfi elementlərinin cəmini : ", cem)
