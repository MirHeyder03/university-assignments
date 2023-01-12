def hesabla():
    cem = 0
    for i in range(1, 101):
        if (cem < 150):
            cem += i
            if (cem > 150):
                cem -= i
    return cem

print(hesabla())
