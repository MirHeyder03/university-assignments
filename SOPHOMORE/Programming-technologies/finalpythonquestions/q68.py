string = input("string-i daxil edin : ")

for i in string:
    if (i.isspace()):
        string=string.replace(i, "*")
print(string)