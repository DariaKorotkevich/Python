from math import floor


def main(x, y, z):
    result = 0
    n = len(x)
    for i in range(0, n):
        result += (13 * (y[floor(i / 3)])**2 + 71 * (x[i]) **
                   3 + (z[(n - 1) + 1 - (floor(i / 2) + 1)]))**6 / 68
    return 74 * result


print(main([0.63, 0.04], [0.78, 0.57], [-0.73, 0.75]))
print(main([0.11, 0.25], [0.19, -0.79], [-0.06, -0.39]))
print(main([0.3, 0.92], [-0.1, 0.02], [0.28, -0.93]))
print(main([0.57, 0.2], [0.12, 0.17], [0.73, -0.27]))
print(main([0.41, 0.08], [0.43, 0.38], [-0.51, 0.29]))
