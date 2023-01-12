string = input("string-i daxil edin : ")
list = []
count = 0
for i in string:
    if not i.isupper():  # ve ya islower
        list.append(i)
        count += 1

print("Setirdeki kicik herfler : ", list)
print("Setirdeki kicik herflerin sayi : ", count)
