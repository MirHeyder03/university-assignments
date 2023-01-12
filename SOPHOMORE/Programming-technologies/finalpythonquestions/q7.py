"""
4 rəqəmli natural ədəd verilmişdir.Bu ədədin yazılışından cüt rəqəmlərin silin.(0 cüt rəqəm kimi qəbul edin)
"""
eded = int(input("4 reqemli tam ededi daxil edin : "))

reqemList = list(map(int, str(eded)))
yeniList = []
for i in range(len(reqemList)):
    if (reqemList[i] % 2 != 0):
        yeniList.append(reqemList[i])

yeniEded = int("".join(map(str, yeniList)))
print(yeniEded)
