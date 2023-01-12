string = input("string-i daxil edin : ")
indexes = [index for index, char in enumerate(string) if char == " "]

print("bosluqlarin indeksleri : ", indexes)
print("bosluqlarin sayi : ", len(indexes))
