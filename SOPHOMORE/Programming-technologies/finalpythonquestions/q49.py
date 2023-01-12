def hesabla():
    hasil = 1
    for i in range(1, 101):
        if (hasil < 1500):
            hasil *= i
            if (hasil > 1500):
                hasil /= i
    return hasil

print(hesabla())
