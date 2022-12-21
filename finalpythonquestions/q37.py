import random
hasil = 1
for i in range(10):
    print(random.randint(0, 100))
    hasil *= random.randint(0, 100)
print(hasil)
