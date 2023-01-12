n = int(input("ededi daxil edin : "))
list = list(str(n))
tekIndex = []
cutIndex = []
for i in range(len(list)):
    if (int(list[i]) % 2 == 0):
        tekIndex.append(list[i])
    if int(list[i]) % 2 != 0:
        cutIndex.append(list[i])

print(tekIndex)
print(cutIndex)

for i in range(len(tekIndex)):
    temp = list[i % 2 == 0]
    list[i % 2 == 0] = list[i % 2 != 0]
    list[i % 2 != 0] = temp


# print(list)
# 21
# temp = 2
# cutİndex = 1
