def main(x):
    if x[4] == 1970:
        return 14
    if x[4] == 2013:
        return 13
    if x[4] == 1989:
        if x[2] == 'CLICK':
            return 12
        if x[2] == 'PHP':
            return Left(x, bro0(x, 7, 8, 9), 10, 11)
        if x[2] == 'UNO':
            return Left(x, bro3(x, 0, 1, 2), 3, bro0(x, 4, 5, 6))


def bro0(x, left, between, right):
    if x[0] == 'RDOC':
        return left
    if x[0] == 'VUE':
        return between
    if x[0] == 'SCSS':
        return right


def bro3(x, left, between, right):
    if x[3] == 'JFLEX':
        return left
    if x[3] == 'SQF':
        return between
    if x[3] == 'RDOC':
        return right


def Left(x, left, between, right):
    if x[1] == 'BOO':
        return left
    if x[1] == 'LESS':
        return between
    if x[1] == 'JSX':
        return right


print(main(['RDOC', 'JSX', 'UNO', 'SQF', 1989]))
print(main(['RDOC', 'JSX', 'UNO', 'JFLEX', 1970]))
print(main(['RDOC', 'BOO', 'CLICK', 'XS', 1989]))
print(main(['RDOC', 'LESS', 'PHP', 'SQF', 1989]))
print(main(['VUE', 'JSX', 'PHP', 'JFLEX', 2013]))
print(main(['VUE', 'BOO', 'UNO', 'JFLEX', 1989]))
