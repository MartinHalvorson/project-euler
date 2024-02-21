# Pentagonal num will mean: 1.5x**2 + 0.5x has root 0.
def is_pentagonal(n):
    a = (0.5 + (0.25 + 6 * n) ** 0.5) / 3
    b = (0.5 - (0.25 + 6 * n) ** 0.5) / 3
    return a == a // 1 and a > 0 or b == b // 1 and b > 0


def is_hexagonal(n):
    a = (1 + (1 + 8 * n) ** 0.5) / 4
    b = (1 - (1 + 8 * n) ** 0.5) / 4
    return a == a // 1 and a > 0 or b == b // 1 and b > 0


for i in range(1065, 1000000):
    tri = i * (i + 1) / 2
    if is_pentagonal(tri) and is_hexagonal(tri):
        print(int(tri))
        exit(0)
