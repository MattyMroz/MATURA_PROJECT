x1 = float(input("Podaj x1: "))
y1 = float(input("Podaj y1: "))
x2 = float(input("Podaj x2: "))
y2 = float(input("Podaj y2: "))
x3 = float(input("Podaj x3: "))
y3 = float(input("Podaj y3: "))


def pole_trjkata():
    return abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) / 2


print(f"Pole trójkąta wynosi: {str(pole_trjkata())}")
