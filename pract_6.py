def main(x):
    if x[3] == 2007:
        if x[4] == 'PERL6':
            return cuba_volt(x, bro2(x, 9, 10), 11)
        if x[4] == 'OPAL':
            return 8
    if x[3] == 2004:
        if x[0] == 1965:
            return 4
        if x[0] == 2008:
            return opal_perl(x, 5, cuba_volt(x, 6, 7))
        if x[0] == 2009:
            return opal_perl(x, bro2(x, 0, 1), bro1(x, 2, 3))


def opal_perl(x, left, right):
    if x[4] == 'OPAL':
        return left
    if x[4] == 'PERL6':
        return right


def cuba_volt(x, left, right):
    if x[1] == 'CUDA':
        return left
    if x[1] == 'VOLT':
        return right


def bro2(x, left, right):
    if x[2] == 1981:
        return left
    else:
        return right


def bro1(x, left, right):
    if x[1] == 1981:
        return left
    else:
        return right


print(main([2009, 'VOLT', 1981, 2007, 'OPAL']))
print(main([1965, 'CUDA', 1981, 2004, 'PERL6']))
print(main([1965, 'CUDA', 1981, 2007, 'PERL6']))
print(main([2009, 'VOLT', 1996, 2004, 'PERL6']))
print(main([2008, 'CUDA', 1996, 2007, 'PERL6']))
