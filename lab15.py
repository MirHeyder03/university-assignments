"""
C(n) ədədi massivinin 5-dən böyük , 15-dən kiçik elementlərinin cəmini hesablayan alqoritm tərtib etməli
"""
n = int(input('Massivin ölçüsünü daxil edin : '))
C = []
for i in range(n):
    C.append(int(input("massivinin elementini daxil edin : ")))

cem = 0
for i in range(len(C)):
    if (C[i] > 5 and C[i] < 15):
        cem += C[i]

print("Massiv : ", C)
print("5-dən böyük , 15-dən kiçik elementlərinin cəmi : ", cem)
