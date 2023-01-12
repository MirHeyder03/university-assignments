from datetime import datetime, timedelta
n = int(input("gunun nomresini daxil edin : "))
m = int(input("ayin nomresini daxil edin : "))
k = int(input("ilin nomresini daxil edin : "))
daxiledilen = datetime(k, m, n)
sabah =daxiledilen + timedelta(days=1)
sabah=sabah.strftime("%d %m %Y")
print(sabah)