# Program sprawdzający czy punkt P nalerzy do trójkąta ABC

# 3 wynaczniki macierzy

# xA = float(input("Podaj xA: "))
# yA = float(input("Podaj yA: "))
# xB = float(input("Podaj xB: "))
# yB = float(input("Podaj yB: "))
# xC = float(input("Podaj xC: "))
# yC = float(input("Podaj yC: "))
# xP = float(input("Podaj xC: "))
# yP = float(input("Podaj yC: "))

xA = 0
yA = 0
xB = 0
yB = 5
xC = 5
yC = 0

xP = 1
yP = 1


def wyznacznik_macierzy(x1, y1, x2, y2, x3, y3):
    return (x3 - y1) * (x2 - x1) - (y2 - y1)*(x3 - x1)


print(wyznacznik_macierzy(xA, yA, xB, yB, xP, yP))
print(wyznacznik_macierzy(xB, yB, xC, yC, xP, yP))
print(wyznacznik_macierzy(xC, yC, xA, yA, xP, yP))


def czy_punkt_nalezy_do_trojkota():
    w1 = wyznacznik_macierzy(xA, yA, xB, yB, xP, yP)
    w2 = wyznacznik_macierzy(xB, yB, xC, yC, xP, yP)
    if w1 * w2 < 0:
        return False
    w2 = wyznacznik_macierzy(xC, yC, xA, yA, xP, yP)
    if w1 * w2 < 0:
        return False
    return True


if czy_punkt_nalezy_do_trojkota():
    print("Punkt należy do trójkąta")
else:
    print("Punkt nie należy do trójkąta")
