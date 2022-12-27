for year in range(1900, 2000):
    for month in range(1, 13):
        for day in range(1, 32):
            if (day * month) == (year % 100):
                print("{0}/{1}/{2} is a magic date!".format(month, day, year))
