N = int(input("N-ni daxil edin : "))

M = list(map(int, str(N)))
M.reverse()
M = int("".join(map(str, M)))
print("M = ",M)
