for num in range(100, 1000):
    cem = 0
    n = 3  # nece reqemli oldugu
    temp = num
    while temp > 0:
        reqem = temp % 10
        cem += reqem ** n
        temp //= 10
    if num == cem:
        print(num)
