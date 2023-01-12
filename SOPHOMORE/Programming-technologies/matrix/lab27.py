"""A matrisinin baş diaqonal elementlərinin cəmini tapmalı."""
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]
     ]

cem = 0
for i in range(len(A)):
    for j in range(len(A[i])):
        if i == j:
            cem += A[i][j]
print(cem)
