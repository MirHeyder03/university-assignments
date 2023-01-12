string = input("string-i daxil edin : ")
list = []
count = 0
for i in string:
    if i.isdigit():
        list.append(i)
        count += 1

print("Setirdeki Reqemler : ", list)
print("Setirdeki reqemlerin sayi : ", count)
