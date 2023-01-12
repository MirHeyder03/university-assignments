N = int(input("ededi daxil edin : "))

def palindrom(eded):
    rev = 0
    i = eded
    while i > 0:
        rev = rev * 10 + i % 10
        i //= 10
    return (eded == rev)

if (palindrom(N)):
    print("Yes")
else:
    print("No")