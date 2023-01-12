string = input("string-i daxil edin : ")
list = []
count = 0
for i in string:
    if i.isupper():
        list.append(i)
        count += 1

print("Setirdeki boyuk herfler : ", list)
print("Setirdeki boyuk herflerin sayi : ", count)
