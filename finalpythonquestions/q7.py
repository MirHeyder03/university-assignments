"""
4 rəqəmli natural ədəd verilmişdir.Bu ədədin yazılışından cüt rəqəmlərin silin.(0 cüt rəqəm kimi qəbul edin)
"""
eded = int(input("4 reqemli tam ededi daxil edin : "))
reqem1 = eded//1000
reqem2 = eded//100 % 10
reqem3 = eded//10 % 10
reqem4 = eded % 10

reqemList = [reqem1, reqem2, reqem3, reqem4]
yeniList = []
for i in range(len(reqemList)):
    if (reqemList[i] % 2 != 0):
        yeniList.append(reqemList[i])


print(yeniList)