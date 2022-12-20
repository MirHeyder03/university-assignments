N = (input("ededi daxil edin : "))
N = str(N)
netice = ""
for i in range(len(N)):
    if (N[i] == N[len(N)-1]):
        netice += N[i]
    else:
        netice += N[i]+"."

print(netice)
