"""
A matrisinin mənfi elementlərinin ən böyüyünü tapın.
"""
A = [[-10, 2, -245], [4, -5, 6], [-7, 8, -9]]
C = []
for i in range(len(A)):
    for j in range(len(A[0])):
        if (A[i][j] < 0):
            C.append(A[i][j])
min=C[0]
for i in range(len(C)):
    if (C[i] > min):
        min = C[i]

print(min)
