# sin1 = 1 - 1/!3 + 1/!5 - 1/!7 + 1/!9 - 1/!11.....


def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n - 1)


print(silnia(4))


def sinus_z_1(x):
    sin = 0
    for i in range(1, 10, 2):
        sin += (-1)**((i-1)/2) * x**i / silnia(i)

    return sin
    return float("{:.4f}".format(sin))
    # return round(sin, 4)


print(sinus_z_1(1))
