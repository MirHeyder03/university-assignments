"""
A(n) ədədi massivinin 9-dan böyük elementlərinin cəmini hesablayan alqoritm tərtib etməli.
"""
n = int(input('Massivin ölçüsünü daxil edin : '))
A = []
for i in range(n):
    A.append(int(input("massivinin elementini daxil edin : ")))

cem = 0
for i in range(len(A)):
    if (A[i] > 9):
        cem += A[i]
print("Massiv : ", A)
print("9-dan böyük elementlərinin cəmi : ", cem)
