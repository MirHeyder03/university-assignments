N = int(input("ededi daxil edin : "))

def isPowerOfTwo(n):
    if (n == 0):
        return False
    while (n != 1):
        if (n % 2 != 0):
            return False
        n = n // 2
    return True

if (isPowerOfTwo(N)):
    print('Yes')
else:
    print('No')
