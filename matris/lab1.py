"""
A matrisinin hər bir sətrindəki maksimum elementi baş diaqonal elementi ilə əvəz etməli.
"""
A = [[1, -2, 3],
     [-4, -5, 6],
     [7, -8, 9]]

min = A[0][0]
for i in range(len(A)):
    for j in range(len(A[0])):
        if (A[i][j] < min):
            min = A[i][j]
print(min)
