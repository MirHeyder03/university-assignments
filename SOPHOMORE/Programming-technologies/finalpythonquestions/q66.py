string = input("string-i daxil edin : ")
list = []
count = 0
for i in string:
    if (not i.isalpha() and not i.isdigit()):
        list.append(i)
        count += 1

print("Setirdeki reqem ve herf olmayan : ", list)
print("sayi : ", count)
