k = int(input("nece reqemli : "))
for num in range(10**(k-1), 10**k):
    cem = 0
    temp = num
    while temp > 0:
        reqem = temp % 10
        cem += reqem ** k
        temp //= 10
    if num == cem:
        print(num)
