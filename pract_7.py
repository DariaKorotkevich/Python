def main(z):
    i = ((z & 511) << 23) | (((z >> 9) & 255) << 15) | (
        ((z >> 22) & 1023) << 5) | ((z >> 17) & 31)
    return str(i)


print(main(int(3271941824)))
print(main(4159801239))
print(main(1203491514))
print(main(3368489402))
# 1618 46 92 50
# 1618 46 92 50
# 1618 46 92 50

# из целой строки в десятичная строка
