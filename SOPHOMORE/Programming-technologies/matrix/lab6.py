# w = 8
# h = 5
# Matrix = [[0 for i in range(w)] for j in range(h)]
# print(Matrix)


# list1 = [1, 2, 3, 4, 5, 6, 7]
# list2 = list(map(lambda x: x*2, list1))
# print(list2)


# list1 = [1, 2, 3, 4]

# def vurma(n):
#     return n * n

# netice = map(vurma, list1)
# print(netice)
# print(list(netice))

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]

# netice = map(lambda x, y: x + y, list1, list2)
# print(list(netice))


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def kvadratıTap(n):
    return n * n

kvadrat = map(kvadratıTap, list1)
netice = list(kvadrat)
print(netice)




