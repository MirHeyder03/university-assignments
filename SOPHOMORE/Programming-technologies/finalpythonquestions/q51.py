import random
list = []

for i in range(0, 100):
    list.append(random.randint(0, 100000))

max = list[0]
for i in range(0, 100):
    if (max < list[i]):
        max = list[i]

print("en boyuk eded : ", max)
print("en boyuk ededin indeksi : ", list.index(max))
