import math
from math import floor


def main(z, x):
    result = 0
    n = len(x)
    for i in range(0, n):
        result += 57 * math.exp(z[floor(i)]**3 / 67 - 38 - x[floor(i)])**4
    return result


print(main([0.18, 0.61, -0.97, 0.98, -0.96, -0.27],
      [-0.02, -0.18, -0.58, -0.76, 0.28, -0.33]))
# print(main([0.57, -0.19, 0.35], [-0.56, 0.64, -0.25], [0.3, -0.67, 0.46]))
# print(main([-0.06, 0.99, 0.25], [-0.1, -0.22, -0.89], [0.87, -0.65, -0.98]))
# print(main([0.48, 0.12, 0.06], [-0.22, -0.39, -0.05], [-0.11, -0.26, -0.77]))
# print(main([-0.42, -0.93, -0.28], [-0.16, 0.28, 0.86], [-0.13, -0.27, -0.61]))
