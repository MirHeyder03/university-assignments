N = int(input("ededi daxil edin : "))
list = []

for i in range(1, N+1):
    if (N % i == 0):
        list.append(i)

print("bolenleri : ", list)
