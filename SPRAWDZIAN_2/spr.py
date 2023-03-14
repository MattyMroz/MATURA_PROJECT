# Liczby Mersenne’a – liczby postaci 2
# n
# -1, gdzie jest liczbą naturalną.
# Liczba Mersenne’a 𝑀𝑛 jest równa sumie ciągu geometrycznego 2
# 0 + 2
# 1 + 2
# 2 + 2
# 3 + ⋯ + 2
# 𝑛−1
# a) Napisz funkcję sprawdzającą czy podana liczba jest liczbą Mensene’a.
# b) Wypisz wszystkie liczby Mensene’a z zadanego przedziału (podajesz n - prawy koniec
# przedziału)

# Zadanie 1

# przykładowe liczby Mersenne'a
# 3 = 2^0 + 2^1 = 3
# 7 = 2^0 + 2^1 + 2^2 = 7
# 15 = 2^0 + 2^1 + 2^2 + 2^3 = 15
# 31 = 2^0 + 2^1 + 2^2 + 2^3 + 2^4 = 31
# 63 = 2^0 + 2^1 + 2^2 + 2^3 + 2^4 + 2^5 = 63
# 127 = 2^0 + 2^1 + 2^2 + 2^3 + 2^4 + 2^5 + 2^6 = 127

# a)
def czy_morsenne(n):
    for i in range(n):
        if 2 ** i - 1 == n:
            return True
    return False

# b)
# n = int(input("Podaj n: "))
# for i in range(1, n):
#     if czy_morsenne(i):
#         print(i)

# Zadanie 2
# Napisz program, który wczyta z klawiatury dwa wielomiany, a następnie wyznaczy wielomian będący ich
# sumą i go wypisze


def sumuj_wielomiany():
    n1 = int(input("Podaj stopień wielomianu 1: "))
    arr1 = []
    for i in range(n1+1):
        a = float(input("a" + str(n1-i) + " = "))
        arr1.append(a)
    print("Wielenomian 1: " + str(arr1))
    n2 = int(input("Podaj stopień wielomianu 2: "))
    arr2 = []
    for i in range(n2+1):
        a = float(input("a" + str(n2-i) + " = "))
        arr2.append(a)
    print("Wielenomian 2: " + str(arr2))

    n = 0
    if n1 > n2:
        n = n1
    else:
        n = n2

    arr3 = []
    # doanie 2 tablic od tylu
    for i in range(n, -1, -1):
        if i > n1:
            # arr3.append(arr2[i])
            # dadaj na początek listy
            arr3.insert(0, arr2[i])
        elif i > n2:
            # arr3.append(arr1[i])
            arr3.insert(0, arr1[i])
        else:
            # arr3.append(arr1[i] + arr2[i])
            arr3.insert(0, arr1[i] + arr2[i])
    # Współczynniki od najwyższego do najniższego
    print("Suma wielomianów: " + str(arr3))


# sumuj_wielomiany()


# Zadanie 3
# 101001
# A0000:A0000:B1001 B11100110


#     Zadanie 3
# Na planecie Kwartacja każda miara jest podzielona na 4 równe części i jej zapis odbywa się w następujący
# sposób: na początku wartości pojawia się duża litera alfabetu A, B, C lub D, określająca odpowiednio
# pierwszą, drugą, trzecią lub czwartą część jednostki, a następnie zapisana w systemie binarnym wartość z
# tej kwarty. Aby przetłumaczyć zapis Kwartacji na zrozumiały dla przeciętnego ziemianina, musimy przeliczyć
# zapis binarny na wartość dziesiętną i umieścić go w odpowiedniej kwarcie jednostki miary. W przypadku
# godziny A jest to pierwsza kwarta, czyli czas od 0 do 14 minut, w przypadku B – 15 do 29 minut, C – 30 do
# 44 minut, D – 45 do 59 minut.
# Przykład 1.
# Jeśli podany zostanie czas:
# a) C11 kwartańskiej godziny, będzie to oznaczało wartość 3 min (112) znajdującą się w trzeciej kwarcie
# godziny, czyli 30 min + 3 min = 33 min;
# b) kwartańska godzina B0110:C1010:A1100, będzie oznaczała 11:40:12 czasu ziemskiego, ponieważ: B0101
# – B to druga kwarta 24-godzinnej doby, która zaczyna się od 6 godziny, a 1012 to 510, otrzymamy więc 11
# godzinę;
# C1010 – C to trzecia kwarta godziny, która zaczyna się od 30 minuty, a 10102 to 1010 , otrzymamy więc 40
# minut;
# A1100 – A to pierwsza kwarta minuty, która zaczyna się od 0 sekundy, a 11002 to 1210, otrzymamy więc 12
# sekund.
# Podobnie wygląda zapis i przeliczanie masy.
# Przykład 2.
# Jeśli podana zostanie masa:
# a) B101 kwartańskiego kilograma, będzie to oznaczało wartość 5 g (1012) znajdującą się w drugiej
# kwarcie kilograma, czyli 250 g + 5 g = 255 g;
# b) C1011101 kwartańskiej tony, będzie to oznaczało wartość 93 kg (10111012) znajdującą się
# w 3 kwarcie tony, czyli 500 kg + 93 kg = 593 kg.
# Ponieważ w fabryce zamontowano urządzenie z innej planety, wszystkie dane w pliku fabryka.txt są
# zapisane w systemie ósemkowym. Pierwszy wiersz stanowi liczbę pomiarów, a każdy kolejny – czas podany
# jako liczby ósemkowe rozdzielone dwukropkiem, oznaczające odpowiednio godziny, minuty i sekundy, oraz
# masę jako jedną liczbę całkowitą, oznaczającą ilość kilogramów czystego kwarcu.
# a) W pliku fabryka.txt są zawarte informacje o ilości czystego kwarcu schodzącego z linii
# produkcyjnej. Ponieważ w pliku dane są zapisane w systemie ósemkowym, napisz translator, który
# przetłumaczy zapis na system kwartański i stworzy jego odwzorowanie w tym systemie.
# 51
# 01:05:30 672
# 01:41:25 720
# 02:06:24 744
with open("./fabryka.txt", 'r') as f:
    lines = f.readlines()
    # 51 to liczba czystego kwarcu
    print("Liczba pomiarów: " + str(lines[0]))
    arr = []
    # zczytaj pozostałe wartości
    for i in range(1, len(lines)):
        arr.append(lines[i].strip().split(" "))
    # print(arr)
    # 01:05:30 zamień z systemu usemkowaego na dziesiętny
    for i in range(1, len(lines)):
        # 01:05:30 podziel na 3 części i każdą zamień na dziesiętny
        arr[i-1][0] = arr[i-1][0].split(":")
        for j in range(0, len(arr[i-1][0])):
            arr[i-1][0][j] = int(arr[i-1][0][j], 8)
        # 672 zamień na dziesiętny
        arr[i-1][1] = int(arr[i-1][1], 8)

        # [[[godzina, minuta, sekunda], gramy]]
    # zapisz kwartalny zapis
    #  godzina:
    #     A od 0 do 5
    #     B od 6 do 11
    #     C od 12 do 17
    #     D od 18 do 23
    # minuta i sekunda:
    #     A od 0 do 14
    #     B od 15 do 29
    #     C od 30 do 44
    #     D od 45 do 59
    # gramy:
    #     A od 0 do 249
    #     B od 250 do 499
    #     C od 500 do 749
    #     D od 750 do 999
    # + dec na bin
    for i in range(0, len(arr)):
        # godzina
        if arr[i][0][0] >= 0 and arr[i][0][0] <= 5:
            arr[i][0][0] = "A" + str(bin(arr[i][0][0]))[2:]
        elif arr[i][0][0] >= 6 and arr[i][0][0] <= 11:
            arr[i][0][0] = "B" + str(bin(arr[i][0][0]))[2:]
        elif arr[i][0][0] >= 12 and arr[i][0][0] <= 17:
            arr[i][0][0] = "C" + str(bin(arr[i][0][0]))[2:]
        elif arr[i][0][0] >= 18 and arr[i][0][0] <= 23:
            arr[i][0][0] = "D" + str(bin(arr[i][0][0]))[2:]
        # minuta
        if arr[i][0][1] >= 0 and arr[i][0][1] <= 14:
            arr[i][0][1] = "A" + str(bin(arr[i][0][1]))[2:]
        elif arr[i][0][1] >= 15 and arr[i][0][1] <= 29:
            arr[i][0][1] = "B" + str(bin(arr[i][0][1]))[2:]
        elif arr[i][0][1] >= 30 and arr[i][0][1] <= 44:
            arr[i][0][1] = "C" + str(bin(arr[i][0][1]))[2:]
        elif arr[i][0][1] >= 45 and arr[i][0][1] <= 59:
            arr[i][0][1] = "D" + str(bin(arr[i][0][1]))[2:]
        # sekunda
        if arr[i][0][2] >= 0 and arr[i][0][2] <= 14:
            arr[i][0][2] = "A" + str(bin(arr[i][0][2]))[2:]
        elif arr[i][0][2] >= 15 and arr[i][0][2] <= 29:
            arr[i][0][2] = "B" + str(bin(arr[i][0][2]))[2:]
        elif arr[i][0][2] >= 30 and arr[i][0][2] <= 44:
            arr[i][0][2] = "C" + str(bin(arr[i][0][2]))[2:]
        elif arr[i][0][2] >= 45 and arr[i][0][2] <= 59:
            arr[i][0][2] = "D" + str(bin(arr[i][0][2]))[2:]
        # gramy
        if arr[i][1] >= 0 and arr[i][1] <= 249:
            arr[i][1] = "A" + str(bin(arr[i][1]))[2:]
        elif arr[i][1] >= 250 and arr[i][1] <= 499:
            arr[i][1] = "B" + str(bin(arr[i][1]))[2:]
        elif arr[i][1] >= 500 and arr[i][1] <= 749:
            arr[i][1] = "C" + str(bin(arr[i][1]))[2:]
        elif arr[i][1] >= 750 and arr[i][1] <= 999:
            arr[i][1] = "D" + str(bin(arr[i][1]))[2:]

    # zapisz do pliku
    with open("./fabryka_kwartalny.txt", 'w') as f:
        f.write(str(lines[0]))
        for i in range(0, len(arr)):
            f.write(str(arr[i][0][0]) + ";" + str(arr[i][0][1]) +
                    ";" + str(arr[i][0][2]) + " " + str(arr[i][1]) + "\n")
