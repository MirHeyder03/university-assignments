import random
list = []

for i in range(0, 100):
    list.append(random.randint(0, 100000))

min = list[0]
for i in range(0, 100):
    if (min > list[i]):
        min = list[i]

print("en kicik eded : ", min)
print("en kicik ededin indeksi : ", list.index(min))
