n = 10


def F(n):
    if n == 0 or n == 1:
        return 1
    else:
        return F(n-1)+F(n-2)


print(F(n)) 