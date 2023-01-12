"""
Mətn sətri verilmişdir.  “a” işarəsi ilə qurtaran sözlərin sayını sayını təyin edin
"""
string = input("string'i daxil edin : ")

metn = string.split(" ")
count = 0
for i in range(len(metn)):
    if (metn[i].endswith("a")):
        count += 1
print(count)