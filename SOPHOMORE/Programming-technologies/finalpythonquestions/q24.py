N = int(input("ededi daxil edin : "))

for i in range(2, N):
    if (N % i == 0):
        print("Eded sade deyil")
        exit()
    else:
        print("Eded sadedir!")
        exit()
