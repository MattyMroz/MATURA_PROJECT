def czy_punkty_sa_po_tej_samej_stronie_prostej():
    # A, B, C - współrzędne punktów
    # x1, y1, x2, y2 - współrzędne punktów
    # Funkcja zwraca True jeśli punkty A, B, C są po tej samej stronie prostej
    # przechodzącej przez punkty x1, y1, x2, y2
    A = float(input("Podaj A: "))
    B = float(input("Podaj B: "))
    C = float(input("Podaj C: "))

    x1 = float(input("Podaj x1: "))
    y1 = float(input("Podaj y1: "))

    x2 = float(input("Podaj x2: "))
    y2 = float(input("Podaj y2: "))

    return (A * x1 + B * y1 + C) * (A * x2 + B * y2 + C) > 0


if czy_punkty_sa_po_tej_samej_stronie_prostej():
    print("Punkty są po tej samej stronie prostej")
else:
    print("Punkty nie są po tej samej stronie prostej")


def czy_punkt_nalerzy_do_odcinka():
    x = float(input("Podaj x: "))
    y = float(input("Podaj y: "))

    x1 = float(input("Podaj x1: "))
    y1 = float(input("Podaj y1: "))

    x2 = float(input("Podaj x2: "))
    y2 = float(input("Podaj y2: "))

    return (y - y1) * (x2 - x1) == (y2 - y1) * (x - x1) and min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2)


if czy_punkt_nalerzy_do_odcinka():
    print("Punkt należy do odcinka")
else:
    print("Punkt nie należy do odcinka")
