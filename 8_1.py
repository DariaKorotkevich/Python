import re


# def main(text):
#     num = re.compile('new[ |\n](\\w+) ?:= ?(\\w+).')
#     return re.findall(num, text)
#
# print(main(
#     'begin [[ new zalabi := esgete_969. ]]. [[ new geer :=teisra. ]]. [[new tela:= rexeat_16 ]].[[ new erce :=lasoat. ]]. end'))
#


def main(text):
    pattern = r"[[ variable list((.?))\s=>\s*(.?\w).\s]]"
    result = re.findall(pattern, text)
    return [(r[1], [int(num) for num in r[0].split('.')]) for r in result]

print(main('begin [[ variable list(-8983 . 6385 )=>aoren_461. ]], [[variable list( -6192 . 4321 . -1780 . 955) =>riuser_156. ]],[[ variable list(-9612 . -2556) =>eres.]], [[ variable list( -9853 . -4639 . -2997) => zaisa_42. ]], \end'))