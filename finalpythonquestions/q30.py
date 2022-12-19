eded = int(input("3 reqemli tam eded daxil edin : "))
reqem1 = eded//100
reqem2 = eded//10 % 10
reqem3 = eded % 10

reqemList = [reqem1, reqem2, reqem3]

reqemList[0]=reqemList[3]
print(reqemList)

# yeniList = []
# for i in range(len(reqemList)):
        # yeniList.append(reqemList[i])
