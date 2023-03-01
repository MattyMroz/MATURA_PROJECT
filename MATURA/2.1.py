# Wiązka zadań Ułamki dwójkowe

def binary(x, k):
    print("0.", end="")
    y = x
    for _ in range(k):
        if y >= 0.5:
            print("1", end="")
        else:
            print("0", end="")
        y = y * 2
        if y >= 1:
            y -= 1


# binary(0.625, 4)

def decymal(x):
    y = 0  # zmienna przechowująca wynik
    k = len(str(x)) - str(x).index('.') - \
        1 if '.' in str(x) else 0  # liczba cyfr po przecinku
    for i in str(x):
        if i == '.':
            continue
        y = y * 2 + int(i)  # mnożenie przez 2 i dodawanie 0 lub 1
    # dzielenie przez 2^k i zaokrąglanie do k miejsc po przecinku
    return round(y / 2**k, k)


# print(decymal(0.101))


# Zadanie 2.1
def binary_1(x, k):
    zmienna_y = []
    print("0.", end="")
    y = x
    for _ in range(k):
        if y >= 0.5:
            zmienna_y.append(round(y, 6))
            print("1", end="")
        else:
            zmienna_y.append(round(y, 6))
            print("0", end="")
        y = y * 2
        if y >= 1:
            y -= 1
    print()
    print(zmienna_y)


# print("Zadanie 2.1")
# binary_1(0.6, 6)


# Zadanie 2.2
def binary_2(x, k):
    zmienna_y = []
    y = x
    for _ in range(k):
        if y >= 0.5:
            zmienna_y.append(round(y, 6))
        else:
            zmienna_y.append(round(y, 6))
        y = y * 2
        if y >= 1:
            y -= 1
    print(zmienna_y)


# Musi to więc być liczba, która w
# rozwinięciu dwójkowym ma dokładnie cztery cyfry po przecinku. Najmniejszą taką liczbą
# jest (0,0001)2, czyli 1/16 = 0,0625.
binary_2(0.0625, 4)
binary_2(0.0625, 3)
print()
binary_2(0.1875, 4)
binary_2(0.1875, 3)
print()
binary_2(0.9375, 4)
binary_2(0.9375, 3)


# 2.3 Rozwiązanie w pdf


