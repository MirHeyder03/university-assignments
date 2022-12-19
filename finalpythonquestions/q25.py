N = int(input("ededi daxil edin : "))

for eded in range(N):
    if eded > 1:
        for i in range(2, eded):
            if (eded % i == 0):
                break
        else:
            print(eded)
