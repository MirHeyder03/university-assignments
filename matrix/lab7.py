"""A matrisinin ən böyük elementini tapmalı."""
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
max = A[0][0]
for i in range(len(A)):
    for j in range(len(A[0])):
        if (max < A[i][j]):
            max = A[i][j]
print("en boyuk eded = ", max)
