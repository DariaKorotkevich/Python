#кортеж из битовых полей

# def main(s):
#     i = int(s)
#     c1 = 0b1111111 & i
#     print(0b1111111)
#     c2 = 0b1111111111 & (i >> 7)
#     c3 = 0b11 & (i >> 17)
#     c5 = 0b111111111 & (i >> 27)
#     return tuple(map(str, (c1, c2, c3, c5)))
#
# print(main('51593330143'))


# hec в  hec
def main(h):
    v = int(h, 16)
    k1 = v & 0x3ff
    k2 = (v >> 10) & 0x3f
    k3 = (v >> 16) & 0
    k4 = (v >> 18) & 0x3f
    k5 = (v >> 24) & 0x3f
    d = k5 | (k1 << 6) | (k2 << 16) | (k3 << 22) | (k4 << 24)
    return str(hex(d))


print(main('0x34058036'))
print(main('0x2a6a334a'))
print(main('0x324bef69'))
print(main('0xe9ab9a1'))



d = {'A': 1, 'B': 2, 'C': 3}

pairs = list(d.items())
print(pairs)