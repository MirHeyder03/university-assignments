eded = int(input("ededi daxil edin : "))

mindigit = min(list(str(eded)))
count = str(eded).count(mindigit)
print("ededdeki en kicik reqem : ", mindigit)
print("nece defe tekrarlanib : ", count)
