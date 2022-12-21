eded = int(input("ededi daxil edin : "))

if (len(str(eded)) < 4 or len(str(eded)) < 0):
    print("eded minlik mertebesine malik olmalidir")
else:
    print(eded//1000 % 10)

