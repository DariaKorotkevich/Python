# import re
#
# #
# # def main(x):
# #     r = r"new\s*(\w+)\s*+:=\s*(\w+)\."
# #     z = re.findall(r, x)
# #     return z
#     # ls2 = []
#     # for ints, key in z:
#     #     ls = []
#     #     for i in ints.split():
#     #         if i == ".":
#     #             continue
#     #         ls.append(int(i))
#     #     p = (key, ls)
#     #     ls2.append(p)
#     # return ls2
#
# #
# # print(main(input()))
#
# import re
#
#
# def main(string):
#     pattern = r"new\s*(\w+)\s*+:=\s*(\w+)\."
#     matches = re.findall(pattern, string)
#     pairs = [(match[0], match[1]) for match in matches]
#     return pairs
#
# # dictionary = dict(pairs)
#     # for key in dictionary:
#     #     dictionary[key] = int(dictionary[key])
# print(main(input()))

# import re
# num = re.compile('new (\\w*).:=([ lt]\\w+)')
# result = 'begin [[ new zalabi := esgete_969. ]]. [[ new geer :=teisra. ]]. [[new tela:= rexeat_16 ]].[[ new erce :=lasoat. ]]. end'
# print(num.findall(result))

import re


def main(x):
    num = re.compile('new (\\w*).:=([ lt]\\w+)')
    return num.findall(x)


print(main(
    'begin [[ new zalabi := esgete_969. ]]. [[ new geer :=teisra. ]]. [[new tela:= rexeat_16 ]].[[ new erce :=lasoat. ]]. end'))
