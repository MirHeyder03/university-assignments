"""
X Y-ə bərabər deyil.2 həqiqi ədəd (X,Y) verilmişdir.Ədədlərin kiçiyini həmin ədədlərin cəminin yarısı ilə , böyüyünü isə bu ədədlərin 2 misli ilə əvəz edin
"""
x = float(input("Enter number X: "))
y = float(input("Enter number Y: "))

if x < y:
    y = (x+y)*2
    x = (x+y)/2
else:
    y = (x+y)/2
    x = (x+y)*2

print("X =", x)
print("Y =", y)
