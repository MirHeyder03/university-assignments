
A = [[-1, -2, 3],
     [4, -5, -6],
     [-7, 8, -9]
     ]
B = []

setir1 = 0
setir2 = 0
setir3 = 0
for i in range(len(A[0])):
    if A[0][i] < 0:
        setir1 += A[0][i]
    if A[1][i] < 0:
        setir2 += A[1][i]
    if A[2][i] < 0:
        setir3 += A[2][i]
B.append(setir1)
B.append(setir2)
B.append(setir3)
print(B)