"""
A(n) ədədi massivinin elementlərinin ədədi ortasını hesablayan alqoritm tərtib etməli
"""
n = int(input('Massivin ölçüsünü daxil edin : '))
A = []
for i in range(n):
    A.append(int(input("massivinin elementini daxil edin : ")))
cem = 0
for i in range(len(A)):
    cem += A[i]
edediOrta = cem/n
print("elementlərinin ədədi ortasını", edediOrta)
