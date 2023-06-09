def remove_none(x):
    res = []
    for row in x:
        if row[0] is None:
            continue
        temp = []
        for cell in row:
            if cell is None:
                continue
            temp.append(cell)
        res.append(temp)
    return res


def remove_duplicates(x):
    output = []
    control = set()
    for row in x:
        if row[0] in control:
            continue
        control.add(row[0])
        output.append(row)
    return output


def formatt(res):
    for row in res:
        row[0] = row[0].split()[1]
        row[1] = row[1].replace('/', '.')[2:]
        row[2] = row[2].replace('N', '0').replace('Y', '1')
        s = row[3]
        row[3] = s[3:6] + '-' + s[6:]
    return res


def transpose(A):
    C = []
    for i in range(len(A[0])):
        ci = []
        for j in range(len(A)):
            a = A[j][i]
            ci.append(a)
        C.append(ci)
    return (C)


def main(x):
    res = remove_none(x)
    res = remove_duplicates(res)
    res = formatt(res)
    res = transpose(res)
    return res



# def main(x):
#     res = filter(len, map(lambda row: list(filter(bool, row)), x))
#     res = map(list, dict.fromkeys(map(tuple, res)))
#     res = [[name.split()[1],
#             date.replace('/', '.')[2:],
#             str('NY'.index(bol)),
#             f'{tel[3:6]}-{tel[6:]}'] for name, date, bol, tel in res]
#     res = [[cell[i] for cell in res] for i in range(len(res[0]))]
#     return res