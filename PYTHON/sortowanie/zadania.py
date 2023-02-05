import random  # losowanie liczb

# Zadanie 1.1:
# Napisz program losujacy tablice n liczb catkowitych z zakresu od —9 do 9 i sortujacy ja niemalejaco wedtug wartosci bezwzgledngj liczb. Sortowanie powinno być stabilne, tzn, elementy réwne co do wartosci bezwzglednej powinny zachowaé kolejności wystepowania w posortowanym ciagu. Na przyktad dla danych:
# -6 5 -1 2 1-1 -5 6 -2


def zad_1_1():
    # Najlepsze rozwiązanie zadania
    n = int(input("Podaj liczbę elementów tablicy: "))
    num = [random.randint(-9, 9) for _ in range(n)]
    print("Tablica: ", num)
    # sorted
    print("Posortowana tablica: ", sorted(num, key=abs))
    print("Posortowana odwrotnie tablica: ",
          sorted(num, key=abs, reverse=True))
    # Sortowanie bąbelkowe
    for i in range(n):
        for j in range(n - i - 1):  # -1 bo nie ma sensu porównywać ostatniego elementu z niczym
            if abs(num[j]) > abs(num[j + 1]):
                num[j], num[j + 1] = num[j + 1], num[j]
            print("i = ", i, "j = ", j, "tablica: ", num)
    print("Posortowana tablica: ", num)


def zad_1_2():
    # Prostrze wersje sortowania bezwzględnego
    n = 9
    tab = [-6, 5, -1, 2, 1, -1, -5, 6, 2]

    # tab = []
    # for i in range(n):
    #     tab.append(random.randint(-9, 9))

    print("Tablica: ", tab)
    print("Posortowana tablica: ", sorted(tab, key=abs))

    # 1 - wersja podstawowa
    tab = [-6, 5, -1, 2, 1, -1, -5, 6, 2]
    for i in range(n):
        for j in range(n - i - 1):
            if abs(tab[j]) > abs(tab[j + 1]):
                tmp = tab[j]
                tab[j] = tab[j + 1]
                tab[j + 1] = tmp
    print("Posortowana tablica: ", tab)

    # 2 - brak zmiennej pomocniczej
    tab = [-6, 5, -1, 2, 1, -1, -5, 6, 2]
    for i in range(n):
        for j in range(n - i - 1):
            if abs(tab[j]) > abs(tab[j + 1]):
                tab[j], tab[j + 1] = tab[j + 1], tab[j]
    print("Posortowana tablica: ", tab)

    # 3 wyjscie z petli
    n = 4
    tab = [1, 3, 2, -1]
    # tab = [-6, 5, -1, 2, 1, -1, -5, 6, 2]
    for i in range(n):
        print("i = ", i, "tablica: ", tab)
        for j in range(n - i - 1):
            if abs(tab[j]) > abs(tab[j + 1]):
                tab[j], tab[j + 1] = tab[j + 1], tab[j]
                print("     j = ", j, "tablica: ", tab,
                      " zamieniono: ", tab[j + 1], tab[j])
            else:
                print("     j = ", j, "tablica: ", tab, " nie zamieniono")
    print("Posortowana tablica: ", tab)


def zad_2():
    # Sortowanie po liczbie jedności z zachowaniem stabilności

    # n = int(input("Podaj liczbę elementów tablicy: "))
    n = 10
    num = [random.randint(0, 100) for _ in range(n)]
    print("Tablica: ", num)

    # sortowanie po reszcie z dzielenia przez 10, czyli ostatniej cyfrze
    print("Posortowana tablica: ", sorted(num, key=lambda x: x % 10))

    for i in range(n):
        for j in range(n - i - 1):  # -1 bo nie ma sensu porównywać ostatniego elementu z niczym
            if num[j] % 10 > num[j + 1] % 10:
                num[j], num[j + 1] = num[j + 1], num[j]
    print("Posortowana tablica: ", num)


def zad_3():
    names = ['kot',  'kapa', 'klacz', 'kopytko',
             'kret', 'kilt', 'kogut', 'komputer', 'kara']
    print("Tablica: ", names)

    print("Posortowana tablica: ", sorted(names, key=len))
    # sortowanie po długości słów z zachowaniem stabilności bąbelkowo
    for i in range(len(names)):
        for j in range(len(names) - i - 1):
            if len(names[j]) > len(names[j + 1]):
                names[j], names[j + 1] = names[j + 1], names[j]
    print("Posortowana tablica: ", names)


def zad_4():
    names = []
    with open("hasla.txt", 'r') as f:
        for line in f:
            names.append(line.strip().split())

    # print("Tablica: ", names)

    names.sort()
    seen = {}  # słownik, gdzie klucz to indeks, a wartość to słowo
    # działa bo lista jest posortowana leksykograficznie słowo po słowie
    result = []
    for sublist in names:
        new_sublist = []
        # i to indeks, word to słowo, enumerate zwraca indeks i wartość
        for i, word in enumerate(sublist):
            # jeśli słowo jest w słowniku i ma tą samą wartość, to zamieniamy na "-"
            if i in seen and word == seen[i]:
                new_sublist.append("-")
            else:
                new_sublist.append(word)
                seen[i] = word
        result.append(new_sublist)

    with open("index.txt", 'w') as f:
        for sublist in result:
            f.write(" ".join(sublist) + "\n")
    print("Słownik: ", seen, "\n")
    print("Zapisano do pliku index.txt: ", result)


def main():
    print("\nZadanie 1.1 - sortowanie bezwzględne z zachowaniem stabilności")
    zad_1_1()
    print("\nZadanie 1.2 - sortowanie bezwzględne ~ zrozumienie algorytmu")
    zad_1_2()
    print("\nZadanie 2 - sortowanie poprzez liczbę jedności z zachowaniem stabilności")
    zad_2()
    print("\nZadanie 3 - sortowanie po długości słów z zachowaniem stabilności")
    zad_3()
    print("\nZadanie 4 - sortowanie leksykograficzne z pliku txt")
    zad_4()


if __name__ == '__main__':
    main()


# Psełdocosie *_*

# import biblioteki random
# funkcja zad_1_1()
#     wczytaj n
#     num = []
#     dla i w zakresie od 0 do n wykonaj
#         do num dodaj losową liczbę całkowitą z zakresu od -9 do 9

#         alternatywnie
#         na końcu num dodaj random.randint(-9, 9)

#     wyświetl: wbydowoną funkcję sorted z parametrem num i kluczem = abs

#     alternatywnie

#     dla i do n wykonaj
#         dla j do n - i - 1 wykonaj
#             jeżeli abs(num[j]) > abs(num[j + 1]) to
#                 num[j], num[j + 1] = num[j + 1], num[j]

# wykonaj zad_1_1()
