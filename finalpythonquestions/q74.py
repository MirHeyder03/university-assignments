n = int(input("ededi daxil edin : "))

def cevir(n):
    if n > 1:
        cevir(n//2)
    print(n % 2, end='')

cevir(n)
